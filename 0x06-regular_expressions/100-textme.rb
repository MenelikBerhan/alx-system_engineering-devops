#!/usr/bin/env ruby
sender=ARGV[0].scan(/\[from:[+\da-z]+\]/i).join
receiver=ARGV[0].scan(/\[to:[+\da-z]+\]/i).join
flags=ARGV[0].scan(/\[flags:[\d:-]+\]/).join

sen=sender.scan(/\+?\b[^(from:)][\da-z]+/i).join
rec=receiver.scan(/\+?\b[^(to:)][\da-z]+/i).join
flg=flags.scan(/-?\b[^(flags:)][\d:-]+/).join

output=sen + ',' + rec + ',' + flg
puts output
