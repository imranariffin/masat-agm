$(function(){
	$(".ask-btn").click(function () {
		var start = "ask-btn-".length;
		var btn_id = String($(this).attr("id"));

		console.log(this);
		console.log($(this));
		
		var asker = $("#asker").val();		
		var cand_id = btn_id.substring(start, btn_id.length);
		var question = $("#question-" + cand_id).val();

		console.log(btn_id + " button clicked!");

		$.ajax({
			type : "POST",
			url : "/tanya",
			data : {
				question : question,
				asker : asker,
				cand_id : cand_id
			},
			success : function (res) {
				// append a new row of 
				console.log(res);
				
				var q = $('<div/>', {class : 'col-md-7'});
				var panel = $('<div/>', {class : 'panel panel-default'});
				var p_header = $('<div/>', {class : 'panel-heading'});
				var p_body = $('<div/>', {class : 'panel-body'});
				panel.append(p_header);				
				panel.append(p_body);
				q.append(panel);
				p_header.text(res.question);
				$("#question-row-" + res.cand_id).append(q);
			},
			error : function (err) {
				console.log(err);
			}
		});
	});
});