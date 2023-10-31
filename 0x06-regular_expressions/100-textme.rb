#!/usr/bin/env ruby
solnn = ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
puts solnn
