# CS361-Add-Subtract-Microservice
## Description
Performs addition or subtraction, then returns the result.

## Calling the Microservice
Make an HTTP GET request to the microservice, specifying either the "add" or "subtract" endpoint. Specify two numbers. For subtraction, the second number will be subtracted from the first number. For addition, the two numbers will be added together.

Example addition:
`https://cs361-add-subtract-microservice.onrender.com/add?num1=4&num2=1`

Example subtraction:
`https://cs361-add-subtract-microservice.onrender.com/subtract?num1=4&num2=1`

Numbers may be decimals or integers. Negative numbers are accepted as well.

## Receiving Data
A JSON object will be returned.

Addition example:
`
{
  "num1": 4,
  "num2": 1,
  "sum": 5
}
`

Subtraction example:
`
{
  "num1": 4,
  "num2": 1,
  "difference": 3
}
`