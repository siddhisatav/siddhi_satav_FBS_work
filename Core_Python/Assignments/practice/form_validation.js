

function is_user_valid(){
    username=document.getElementById("username").value
    if (username.trim().length == 0){
        document.getElementById("username_error").innerHTML="Username cannot be empty"
        return false
    }
    else{
        document.getElementById("username_error").innerHTML=""
        return true
    }
    
}   

function is_password_valid(){
    passw = document.getElementById("password").value
    
    if (passw.trim().length == 0){
        document.getElementById("password_error").innerHTML="Password cannot be empty"
        return false
    }


    else if (passw.length < 5){
        document.getElementById("password_error").innerHTML="Password must be at least 5 characters long"
        return false
    }
    else{
        document.getElementById("password_error").innerHTML=""
        return true
    }
}


function valid_course(){
    course=document.getElementsByName("course")
    for (var i = 0; i < course.length; i++){
        if (course[i].checked){
            return true
        }
    }

   
    document.getElementById("course_error").innerHTML="Please select at least one course"
    return false;
}

function valid_gender(){
    gender=document.getElementsByName("gender")
    for (var i = 0; i < gender.length; i++){
        if (    gender[i].checked){
            document.getElementById("gender_error").innerHTML=""
            return true
        }
    }
    document.getElementById("gender_error").innerHTML="Please select a gender"
    return false;
}

function valid_terms(){
    terms=document.getElementById("terms")
    if (terms.checked){
        document.getElementById("terms_error").innerHTML=""
        return true
    }
    else{
        document.getElementById("terms_error").innerHTML="Please agree to the terms and conditions"
        return false
    }
}

function form_validationnn(){

    if (is_user_valid() && is_password_valid() && valid_course() && valid_gender() && valid_terms()){
        document.getElementById("reg_form").submit();
        return true
    }
    return false

}
