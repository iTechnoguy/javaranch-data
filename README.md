# javaranch-data
Cleaning up and formatting java questions from the [java ranch roundup game](http://www.javaranch.com/roundup.jsp). Want to use the data? Look [here](http://seanastephens.github.io/javaranch-data/questions.json).

# JSON Layout

    [
      {
       "id": "1",
       "line": "A string question related to some detail of java",
       "answer": "A string answer to the line element question",
       "explanation": "A string explanation as to why the answer is correct",
       "bogus": [
          "An array of incorrect string answers"
        ]
      }
    ]

# V2 JSON Layout

    [
      {
       "id": "1",
       "question": "A string question related to some detail of java",
       "answers": [
          {
           "answer": "A string multiple choice answer to the question",
           "correct": "truthy value if this is the correct answer"
          }
        ]
       "explanation": "A string explanation as to why the answer is correct",
      }
    ]
