# Specification of the `pathways.json` file

`pathways.json` is a JSON object with the top-level keys being the
title of the given HASS pathway and the values described below.

| Field              | Type   | Description                                                       | Example                                                                                     |
|--------------------|--------|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| `description`      | String | Description of the pathway                                        | `"This pathway allows students to study..."`                                                |
| `minor`            | Array  | The minors this pathway can be used for                           | `[ "General Psychology Minor", "Psychological Science Minor" ]`                             |
| `one_of`           | Object | The courses you must take at least one of to complete the pathway |                                                                                             |
| `remaining`        | Object | The set of "remaining" courses (details below)                    |                                                                                             |
| `remaining_header` | String | Human-readable string description of the remaining courses        | `"Choose remaining credits from the following, with at least 4 credits at the 4000-level:"` |
| `required`         | Object | The courses you are required to take to complete the pathway      |                                                                                             |

## `one_of`, `remaining` and `required`

All three of these fields follow the same format: keys are the course
name (e.g. `"Behavioral Neuroscience"`) and values are the course code
(e.g. `"PSYC4360"`). At least one of these fields must be present,
otherwise they are optional. An example:

```json
{
    "Art History": "ARTS1050",
    "Histories of Jazz and Improvised Music": "ARTS2510",
    "History of Animation": "IHSS1170",
    "Race and Film in U.S. Culture and History": "IHSS1300",
    "Songwriting Workshop": "IHSS1700"
}
```

## Complete example

```json
{
    "Public Health": {
        "description": "The pathway in Public Health is designed for students interested in health-related careers...",
        "minor": [
            "Public Health Minor"
        ],
        "one_of": {
            "Introduction to Psychological Science": "PSYC1200",
            "Science, Technology, and Society": "STSO1110",
            "The Genome and You": "IHSS1150"
        },
        "remaining": {
            "Bioethics": "STSO4250",
            "Drugs in History": "STSO4430",
            "Drugs, Society, and Behavior": "PSYC4500",
            "Food, Farms, and Famine": "STSO4260",
            "Gender, Science, and Technology": "STSO4560",
            "History of Medicine": "STSO4420",
            "History of Mental Health": "STSO4440",
            "Hormones, Brain, and Behavior": "PSYC4700",
            "Medicine, Culture, and Society": "STSO4400",
            "Stress and the Brain": "PSYC4610"
        },
        "remaining_header": "Choose remaining credits from the following:",
        "required": {
            "Sociology": "STSO2520"
        }
    }
}
```
