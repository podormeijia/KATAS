class Conjurer
  def self.conjure (name,f)
    define_method(name) do
      p f.call()
    end
  end
end

def cap_me ary
  ary.each do |x|
    x.to_s.capitalize!
  end
end

def domain_name(url)
  url =~ %r[(http|https)://+(www.)*(.+)(.com)+|]
  Regexp.last_match[3]
end


class Hash
  def get_value( default, *args )
    res = self
    args.each do |argument|
      if !(res.is_a?Hash) || res[argument].nil?
        next res = self
      end
      res = res[argument]
    end
    if res == self
      return default
    else
      return (default+res).to_s(16).hex if res.is_a?Fixnum
      return res.to_s
    end
  end
end

def sortme( names )
  names.sort do |a, b|
    a.downcase <=> b.downcase
  end
end

#Code Learning
class Calc
  { zero: 0, one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9 }.each do |m, n|
    define_method("#{m}") { @proc ? @proc.call(n) : (@number ||= n ; self ) }
  end

  { plus: :+, minus: :-, times: :*, divided_by: :/ }.each do |m, o|
    define_method("#{m}") { @proc ||= lambda { |a| @number.send(o, a) }; self }
  end
end

def domain_name(url)
  regex = /(http|https):\/\/(?:www\.)?(?<domain_name>.*?)\./
  url.match(regex)[:domain_name]
end

class Object
  %w[zero one two three four five six seven eight nine].each_with_index do |name, n|
    define_method(name) do |args = nil|
      args ? n.send(*args) : n.to_f
    end
  end

  %w[plus + minus - times * divided_by /].each_slice(2) do |name, symbol|
    define_method(name) do |n|
      [symbol, n]
    end
  end
end

class Hash
  def get_value( default, *args )
    args.empty? ? default : args.reduce(self) { |acum, key| acum.fetch(key) } rescue default
  end
end

def sortme( names )
  names.sort_by(&:downcase)
end