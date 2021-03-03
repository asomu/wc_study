var product = {
    name:'kim',
    age:50,
    address:'seoul'
};

var person = {
    name:'kim',
    eat:function(food){
        alert(this.name + '이/가 ' + food + '를 먹습니다.');
    }
}

person.eat('바나나');
window.onload = function(){
    document.querySelector('h1').style.background='red';
    document.querySelector('h2').style.color='blue';
}

