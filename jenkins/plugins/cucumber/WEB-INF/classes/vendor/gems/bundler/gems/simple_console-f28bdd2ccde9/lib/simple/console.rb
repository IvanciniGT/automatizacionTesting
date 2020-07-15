require 'term/ansicolor'

class Simple
  class Console
    VERSION = '0.0.1'

    include Term::ANSIColor

    attr_accessor :color_output
    
    def initialize args = {}
        @color_output = args[:color_output] || 'false'
    end

    def info(message, args={})
        if @color_output == true
            if args[:title].nil? || args[:title].empty?
                string = "#{bold(black(blue("#{message}")))}"
            else
                string = "#{black(red(bold("#{args[:title]}:")))} #{bold(black(blue("#{message}")))}"
            end
        else
            if args[:title].nil? || args[:title].empty?
                string = "#{message}"
            else
                string = "#{args[:title]}: #{message}"
            end
        end
        string
    end

    def error(message)
        string = @color_output == true ? "#{bold(red("ERROR: #{message}"))}" : "ERROR: #{message}"
    end

  end
end

