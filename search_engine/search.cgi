#! /usr/bin/env python3
print ("Content-type: text/html")
import cgi
import retrieval
import cgitb
cgitb.enable()

print ("""
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Synap</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="styles.css">
    <script src="https://use.fontawesome.com/3a06ef9cbd.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
    <script src="script.js"></script>
</head>
<body>
    <div class="top container">
        <img src="Logo.png" alt="Synap Logo">
        <div class="container__item">
            <form action="search.cgi" method="get" class="form">
                <input type="text" class="form__field" name="words" placeholder="Releave Your Synaps" />
                <input type="submit" class="btn btn--primary btn--inside uppercase"/>
            </form>
        </div>
    </div>
    <div class="bottom container">
        <div id="list2">
            <ol>
""")

form = cgi.FieldStorage()
term = form.getvalue("words")
term = str(term)
arr = term.split()
print("<p> You searched for: " + term + "</p>")
results = retrieval.retrieval("or", term)

for url in results:
    print ("<li><p>" + str(url[0]) + " <a href=\"" + url[1] + "\">" + url[2] + "</a></p></li>")
print("""</ol>
         </div>
    </div>
</body>
</html>
""")
