// function sendmail(){
//     var params={
//         name: document.getElementById("name").ariaValueMax,
//         number: document.getElementById("number").ariaValueMax,
//         email: document.getElementById("email").ariaValueMax,
//         pincode: document.getElementById("pincode").ariaValueMax,
//         state: document.getElementById("states").ariaValueMax,
//         requirements: document.getElementById("comments").ariaValueMax




//          };

//         console.log('params')
//         console.log(params)
//     const serviceID="service_3jv3erl";
//     const templateID="template_46ed5gi";
//     emailjs.send(serviceID,templateID,params)
//     .then((res)=>{
//         document.getElementById("name").value="";
//         document.getElementById("number").value="";
//         document.getElementById("email").value="";
//         document.getElementById("pincode").value="";
//         document.getElementById("states").value="";
//         document.getElementById("comments").value="";
//         console.log(res);
//         alert("you successfully submit the form");
//        })
//     .catch((err)=>console.log(err));
// }



function sendmail(event) {
    event.preventDefault()
    console.log('Sending mail...');

    var params = {
        name: document.getElementById("name").value,
        number: document.getElementById("number").value,
        email: document.getElementById("email").value,
        pincode: document.getElementById("pincode").value,
        state: document.getElementById("states").value,
        comments: document.getElementById("comments").value,
    };

    const serviceID = "service_3jv3erl";
    const templateID = "template_46ed5gi";
    emailjs.send(serviceID, templateID, params)
        .then((res) => {
            document.getElementById("name").value = "";
            document.getElementById("number").value = ""; 
            document.getElementById("email").value = "";
            document.getElementById("pincode").value = "";
            document.getElementById("states").value = "";
            document.getElementById("comments").value = "";
            console.log(res);
            alert("you successfully submit the form");
        })
        .catch((err) => console.log(err));
}





