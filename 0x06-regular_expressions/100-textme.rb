#!/usr/bin/env ruby
matches = ARGV[0].match(/\[from:(?<from>.*?)\] \[to:(?<to>.*?)\] \[flags:(?<flags>.*?)\]/)
puts "#{matches[:from]},#{matches[:to]},#{matches[:flags]}" if matches
