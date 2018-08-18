$(function(){
	content = 'siboer';
	$('.panel-button').on('click',function(){
		var panelId = $(this).attr('data-panelid');
		//$('#'+panelId).toggle();
		$('#'+panelId+' .card-text').html(content);
	})
})


function add(first,second,callback){
	console.log(first+second);
	callback();
}

add(2,3,function(){
	console.log('done');
})

//scope == variable access
var a = 1;
var b = 1;
function foo(){
	var a = 2;
	b = 3;
	console.log(window.a);
	console.log(a);
}
foo();
console.log(a);
console.log(b);

//context == this

console.log(this);
function boo(){
	console.log(this);
}

window.boo();

var my_obj = {
	foo: function(){
		console.log(this);
	}
};
//my_obj.foo();

// call,apply,bind

my_obj.foo.call(window,1,2,3);

$('li').on('click',function(){
	var currenttTimes = parseInt( $(this).find('span').html());

	$(this).find('span').html(currenttTimes+1);
	//console.log(currenttTimes);
});

$(function(){
	var $orders = $('#orders');
	var $name = $('#name');
	var $drink = $('#drink');

	var orderTemplate = "" +
	"<liname: {{name}},drink: {{drink}}</li>";

	function addOrder(order){
		$order.append(Mustache.render(orderTemplate,order));
		//$orders.append('<li>name:' + order.name + ', drink: ' + order.drink + '</li>');
	}

	$.$.ajax({
		url: '/api/orders',
		type: 'GET',
		dataType: 'default: Intelligent Guess (Other values: xml, json, script, or html)',
		data: {param1: 'value1'},
	})
	.done(function() {
		console.log("success");
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
	
})