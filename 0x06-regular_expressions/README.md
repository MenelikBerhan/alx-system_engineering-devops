# __0x06-regular_expressions__

## 0-simply_match_school.rb

a Ruby script that accepts one argument and pass it to a regular expression matching method that matches the word `School`

## 1-repetition_token_0.rb

a Ruby script that accepts one argument and pass it to a regular expression matching method that matches:

- `hbttn`
- `hbtttn`
- `hbttttn`
- `hbtttttn`

but skips:

- `hbn`
- `hbtn`
- `hbttttttn`

## 2-repetition_token_1.rb

a Ruby script that accepts one argument and pass it to a regular expression matching method that matches:

- `htn`
- `hbtn`

but skips:

- `hbbtn`
- `hbbbtn`

## 3-repetition_token_2.rb

a Ruby script that accepts one argument and pass it to a regular expression matching method that matches:

- `hbtn`
- `hbttn`
- `hbtttn`
- `hbttttn`

but skips:

- `hbn`

## 4-repetition_token_3.rb

a Ruby script that accepts one argument and pass it to a regular expression matching method that matches:

- `hbn`
- `hbtn`
- `hbttn`
- `hbtttn`
- `hbttttn`

but skips:

- `hbon`

## 5-beginning_and_end.rb

a Ruby script that accepts one argument and pass it to a regular expression matching method that matches a string that starts with `h` ends with `n` and can have any single character in between.

## 6-phone_number.rb

a Ruby script that accepts one argument and pass it to a regular expression matching method that matches a 10 digit phone number.

## 7-OMG_WHY_ARE_YOU_SHOUTING.rb

a Ruby script that accepts one argument and pass it to a regular expression matching method that matches capital letters only.

## 100-textme.rb

a Ruby script that accepts one argument of a log file line and outputs:
`[SENDER],[RECEIVER],[FLAGS]`

- The sender phone number or name (including country code if present)
- The receiver phone number or name (including country code if present)
- The flags that were used

- Example:

```bash
./100-textme.rb 'Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'
Google,+16474951758,-1:0:-1:0:-1
```
