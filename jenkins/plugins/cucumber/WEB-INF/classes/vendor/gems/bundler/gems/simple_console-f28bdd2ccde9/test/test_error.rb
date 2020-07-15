require File.join(File.dirname(__FILE__), '/test_helper.rb')

class SimpleConsoleTest < MiniTest::Unit::TestCase
    def test_colorless_error
        assert_equal "ERROR: message",
            Simple::Console.new(:color_output => false).error('message')
    end
end
