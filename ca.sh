#!/bin/bash
scrapy crawl amz -o data.csv -t csv
cat data.csv
