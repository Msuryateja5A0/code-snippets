<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration form</title>
    <style>
        body{
            font-family:Arial, Helvetica, sans-serif;
            background-color: #f2f2f2;
            padding: 20px;
            background-image: url("bg.img");
        }
        .container{
            background-color: pink;
            padding: 20px;
            border-radius: 5px;
            margin:auto
        }
        .contain h2{
            text-align: center;
        }
        .form-group{
            margin-bottom: 15px;
        }
        .form-group label{
            display: block;
            margin-bottom: 5px;
        }
        .form-group input{
            width: 95%;
            padding: 10px;
            border:1px solid;
            border-radius: 5px;
        }
        .form-group input[type="button"]{
            background-color: #4CAf50;
            color: white;
            border: none;
            cursor: pointer;
            width:100%;
        }
        .form-group input[type="button"]:hover{
            background-color: #45a049;
        }
        form{
            padding:10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Registration form</h2>
        <form id="reg form">
            <div class="form group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name">
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email">
                </div>
                <div class="form-group">
                    <label for="phone">Phone:</label>
                    <input type="tel" id="phone" name="phone">
                </div>
                <div class="form-group">
                    <input type="button" on click="validationform()" value="Register">

                </div>
            </div>
        </form>

    </div>
    <script>
        var email=document.getElementById('email').value.trim();
        var phone=document.getElementById('phone').value.trim();
        var errormeassage=" ";
        if(name==' '){
            error.message+='please enter name\n';

        }
        if(email==' '){
            error.message+='please enter email\n';
            
        }
        if(phone==' '){
            error.message+='please enter Phone number\n';
            
        }
        if(errormeassage==' '){
            alert(errormessage);
            return false;
            
        }
        alert('form submitted successfully');
        window.location.href='success message.html'
    </script>
    
</body>
</html>
