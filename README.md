# PlusSize

Find out which log files are grows very fast.

## Installation
`pip3 install plussize`

## Examples

Which log file grows faster in /var/log for next 5 seconds:

`pluss -t 5 /var/log/ | tail`

## Options

`-l` - count lines, not just bytes (takes longer time)

`-r` - recursive

`-t` - time difference (in seconds) between two checks. Default: 20

`-z` - print files with zero increment
