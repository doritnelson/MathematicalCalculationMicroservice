### Mathematical Calculation Microservice (Microservice 4)

This microservice performs basic mathematical operations for any main program. It monitors a file named calculation.txt, reads JSON requests written by a client program, processes each requested calculation, and overwrites the file with the results.
All communication happens through this shared file — the client and microservice never call each other directly.

## How to Request Data

To request calculations, the client program writes a JSON object into calculation.txt.
The JSON must contain a request list, where each item describes one operation.

Each operation includes:

action — the type of calculation

int_array — the integers used in the calculation

Supported Actions
Action	Description
total	Adds all numbers together
average	Calculates the average of all numbers
difference	Absolute difference of the first two numbers
Example Request
{
  "request": [
    { "action": "total", "int_array": [2, 5, 2, 7] },
    { "action": "average", "int_array": [2, 5, 2, 7] },
    { "action": "difference", "int_array": [2, 4] },
    { "action": "not_an_action", "int_array": [2, 4, 2, 7] },
    { "actio": "total", "int_array": [2, 4, 2, 7] }
  ]
}


Invalid or misspelled actions still receive responses, but they are returned with error messages.

## How to Receive Data

After the microservice processes the request, it replaces calculation.txt with a JSON array of result objects.
Each result corresponds to one item in the original request.

Response Format
{
  "completed": true or false,
  "result": <number>,
  "error": "None" or "<error message>"
}

Example Response
[
  { "completed": true,  "result": 16, "error": "None" },
  { "completed": true,  "result": 4,  "error": "None" },
  { "completed": true,  "result": 2,  "error": "None" },
  { "completed": false, "result": 0,  "error": "Action not in list of available functions" },
  { "completed": false, "result": 0,  "error": "Incomplete action - error thrown" }
]

## How to Run the Microservice

Make sure calculation.txt exists in the same folder as the microservice code.

Open two terminals.

Terminal 1 — Start the Microservice
python mathematical_calculation_microservice.py

Terminal 2 — Run the Test Program
python calculation_test.py


The microservice will detect the file change, process all calculations, and overwrite the file with the results.

Example Test Program (Client)
import json

calculation_request = {
    "request": [
        {"action": "total", "int_array": [2,5,2,7]},
        {"action": "average", "int_array": [2,5,2,7]},
        {"action": "difference", "int_array": [2,4]}
    ]
}

with open("calculation.txt", "w") as f:
    json.dump(calculation_request, f, indent=4)


## Notes

The file must exist before the microservice starts.

Each operation in the request is handled separately, so one invalid item does not stop the others.

The client and microservice never call each other directly — all communication is done through calculation.txt.

<img width="802" height="368" alt="image" src="https://github.com/user-attachments/assets/2b349aea-b9a9-45d9-8c79-ec10781eda0e" />


## Contributions

Dorit: Created the microservice and fully tested the code. Also created the initial README file.
Kaedin: Completed the final README file, performed additional testing, and created the demo video for the microservice.
