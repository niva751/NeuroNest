// Canvas Draw
const canvas=document.getElementById("draw");
const ctx=canvas.getContext("2d");
let draw=false;
canvas.onmousedown=()=>draw=true;
canvas.onmouseup=()=>draw=false;
canvas.onmousemove=e=>{
    if(draw){ctx.fillRect(e.offsetX,e.offsetY,4,4);}
}
function clearCanvas(){ctx.clearRect(0,0,canvas.width,canvas.height);}
async function sendDrawing(){
    const blob=await new Promise(res=>canvas.toBlob(res));
    let form=new FormData(); form.append("image",blob);
    const res=await fetch("/ml/draw/",{method:"POST",body:form});
    const data=await res.json();
    alert("Similarity: "+data.similarity+"%");
}

// Chat
let chatSocket=new WebSocket('ws://'+window.location.host+'/ws/chat/');
chatSocket.onmessage=function(e){
    const data=JSON.parse(e.data);
    document.getElementById("chat-box").innerHTML+="<p>"+data.message+"</p>";
}
function sendMessage(){
    const msg=document.getElementById("msg").value;
    chatSocket.send(JSON.stringify({'message':msg}));
    document.getElementById("msg").value="";
}
