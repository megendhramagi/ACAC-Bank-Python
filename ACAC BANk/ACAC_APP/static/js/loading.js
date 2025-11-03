var result=false
    result="{{ isOk }}"
    console.log(result)
    //make sure js after html loaded
    document.addEventListener("DOMContentLoaded",function(){

      if(result=="True"){
        document.getElementById("result").innerHTML="Registration successfull..Login to continue";
        
          setTimeout(function(){
            window.location.href="{% url 'login' %}"
          },6000); //to redirectto login if condition is true
      }else if(result=="False"){
        document.getElementById("result").innerHTML="Registration Failed..Try Again";
        
          setTimeout(function(){
            window.location.href="{% url 'register' %}"
          },6000); //to redirectto reg if condition is false
      }
    });