
const darkBtn = document.getElementById('darkBtn');
darkBtn.onclick = function(){
    document.body.classList.toggle('dark');
}


const helloBtn = document.getElementById('helloBtn');
helloBtn.onclick = function(){
    alert('网页运行成功！');
}