#!/bin/python3

import os
import requests

#
# Complete the 'healthCheckup' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER lowerLimit
#  2. INTEGER upperLimit
#
# API URL: https://jsonmock.hackerrank.com/api/medical_records?page={page_no}
#

def healthCheckup(lowerLimit, upperLimit):
    url = "https://jsonmock.hackerrank.com/api/medical_records"
    count = 0
    page = 1
    total_pages = 1
    while page <= total_pages:
        response = requests.get(f"{url}?page={page}")
        body = response.json()
        total_pages = body['total_pages']
        for record in body['data']:
            diastole = record['vitals']['bloodPressureDiastole']
            if lowerLimit <= diastole <= upperLimit:
                count += 1
        page += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lowerLimit = int(input().strip())
    upperLimit = int(input().strip())

    result = healthCheckup(lowerLimit, upperLimit)

    fptr.write(str(result) + '\n')

    fptr.close()
