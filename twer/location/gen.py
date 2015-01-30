import csv
from xpinyin import Pinyin

class Generator(object):
    '''
        1. parse names.csv; Name en, cn
        2. parse en.suggustions.csv; Suggestion city, state, postal popularity
        3. build Locations; find name => suggustions.csv, Location(state,city,popularity,postal){en,cn} [ mapping state]
        4. generate firstLine; generate secondLine
        5. remove duplicated in zh.suggestions; generate new csv
        6. write gen.txt
        7. you should apend gen.txt to new csv Manually
    '''
    def __init__(self):
        self.pinYin = Pinyin()

    def generate(self):
        suburbs = self.parse_suburbs()
        print("%d suburbs has read" %len(suburbs))

        suggstions = self.parse_suggestions()
        print("%d suggestions has read" %len(suggstions))

        locations = []
        for suburb in suburbs:
            if suburb.en.lower() not in suggstions:
                print("the suburb %s is not found"  %(suburb.en))
                continue
            locations.append(self.build_location(suburb, suggstions[suburb.en.lower()]))
        print("%d locations has built" %len(locations))

        self.dedup(locations)
        with open('out_gen.txt', 'w') as txtfile:
            for location in locations:
                txtfile.write(self.gen(location))
                txtfile.write('\n')

    def parse_suburbs(self):
        suburbs = []
        spamReader = csv.reader(open('suburbs.csv', newline=''), delimiter=',')
        for row in spamReader:
            suburbs.append(Name(row[0],row[1]))
        return suburbs

    def parse_suggestions(self):
        suggestions = {}
        spamReader = csv.reader(open('suggestions_en.csv', newline=''), delimiter=',', quotechar='"')
        for row in spamReader:
            suggestion = self.do_parse_suggestion(row)
            suggestions[suggestion.city.lower()] = suggestion
        return suggestions

    def do_parse_suggestion(self,row):
        ary1 = row[0].split(',')
        ary2 = ary1[1].strip().split(' ')
        return Suggestion(ary2[0], '', ary1[0], row[1]) if len(ary2) == 1 else Suggestion(ary2[0], ary2[1], ary1[0], row[1])

    def mapping_state(self,state):
        states = {"act":"首都领地", "wa":"西澳大利亚州", "nt":"北领地", "tas":"塔斯马尼亚", "qld":"昆士兰", "vic":"维多利亚州", "nsw":"新南威尔士州", "sa":"南澳大利亚州"}
        return states[state.lower()]

    def build_location(self, suburb, suggestion):    
        state = Name(suggestion.state, self.mapping_state(suggestion.state))
        postal = suggestion.postal
        city = Name(suggestion.city, suburb.zh)
        popularity = suggestion.popularity
        return Location(state,postal,city,popularity)

    def gen(self, location):
        firstLine = "\"%s%s, %s\",%s,\"%s, %s %s\"" % (location.state.zh, location.city.zh, location.postal, 
                                                       location.popularity, 
                                                       location.city.en, location.state.en.upper(), location.postal)
        secondLine = "\"%s\",%s,\"%s%s, %s;%s, %s %s\"" % (self.parse_pinyin(location.state.zh, location.city.zh), 
                                                       location.popularity, 
                                                       location.state.zh, location.city.zh, location.postal,
                                                       location.city.en, location.state.en.upper(), location.postal)
        return '\n'.join([firstLine, secondLine])

    def parse_pinyin(self, state, city):
        state = self.pinYin.get_pinyin(state, '')
        city =  self.pinYin.get_pinyin(city, '')
        return ' '.join([state,city])

    def dedup(self, locations):
        # popularities = [location.popularity for location in locations]
        conditions = ['-'.join([location.city.en.lower(), location.state.en.lower(), location.postal]) for location in locations]
        print("conditions' size is %d" %len(conditions))
        with open('suggestions_zh.csv', newline='') as in_file, open('out_suggestions_zh.txt', 'w') as out_file:
            spamreader = csv.reader(in_file, delimiter=',', quotechar='"')
            num = 0
            canCopy = True
            for row in spamreader:
                line = "\"%s\",%s,\"%s\"" % (row[0],row[1],row[2])
                num = num + 1
                # print("%d, postaled line: %s" % (num,line))
                if canCopy or num%2 == 1:
                    if num % 2 == 1:
                        condition = self.get_city_and_postal_and_state(row)
                        if condition in conditions:
                            print(line)
                            canCopy = False
                        else:
                            canCopy = True
                            postal = ''
                            if len(condition.split('-')) == 3 and not condition.split('-')[2] == '':
                                postal = ", %s" %condition.split('-')[2]
                            line = "\"%s%s\",%s,\"%s\"" % (row[0], postal, row[1], row[2])
                else:
                    print(line)

                if canCopy:
                    out_file.write(line)
                    out_file.write('\n')

    def get_city_and_postal_and_state(self, row):
        ary1 = row[2].split(',')
        if not len(ary1) == 1:
            ary2 = ary1[1].strip().split(' ')
            if not len(ary2) == 1:
                return '-'.join([ary1[0].lower(), ary2[0].lower(), ary2[1]])
        return '-'.join([ary1[0].lower(), '', ''])

class Name(object):
    def __init__(self, en, zh):
        self.en = en
        self.zh = zh

class Suggestion(object):
    def __init__(self, state, postal, city, popularity):
        self.state = state
        self.postal = postal
        self.city = city
        self.popularity = popularity

class Location(object):
    def __init__(self, state, postal, city, popularity):
        self.state = state
        self.postal = postal
        self.city = city
        self.popularity = popularity
        
Generator().generate()
