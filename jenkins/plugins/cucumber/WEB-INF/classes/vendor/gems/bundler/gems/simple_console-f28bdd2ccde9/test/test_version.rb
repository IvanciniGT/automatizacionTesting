require File.join(File.dirname(__FILE__), '/test_helper.rb')

describe Simple::Console do
 
  it "must be defined" do
    Simple::Console::VERSION.must_equal '0.0.1'
  end
 
end
