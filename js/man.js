function shuffle(o){ //v1.0
    for(var j, x, i = o.length; i; j = Math.floor(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
    return o;
};

$(function() {
	var dream = {};
	var people = new Array();
	var makeCopy = new Array();

	$.ajax({
		type: "GET",
		url: '/man',
		success: function (data) {
			$.each(data, function(i, candidate) {
				console.log(candidate.manifesto);
				$.each(candidate.manifesto, function(i, man) {
					if (man[0] != '1' && man[0] != '2' && man[0] != '3') {
						var temp = {'name':candidate.name,
										'position':candidate.position,
										'manifesto':man[0]};
						makeCopy.push(temp);

					}
				});
			});
			shuffle(makeCopy);
			makeCopy.sort(function (a,b) {
				if (a.position > b.position) return 1;
				if (a.position < b.position) return -1;
				return 0;
			});
			$.each(makeCopy, function(i, candidate) {
				$('#mlist').append(
				'<a href="#1" class="list-group-item" data-pos="' +
			     candidate.position +
			     '" data-name="' +
			     candidate.name + 
			     '"><span class="badge">' + 
			     candidate.position  +
			     '</span>' +
			     candidate.manifesto +
			     '</a>'
			    );
			});

			$('a').click(function() {
				var $aClass = $(this)
				var index = -1;
				var maxList =   [{'position':'President', 'max':0}, 
									  {'position':'VP', 'max':0}, 
									  {'position':'Secretary', 'max':0}, 
									  {'position':'Treasurer', 'max':0}, 
									  {'position':'Media', 'max':0}, 
									  {'position':'Sports', 'max':0}, 
									  {'position':'PR', 'max':0}, 
									  {'position':'Cultural', 'max':0}, 
									  {'position':'YearRep4', 'max':0}, 
									  {'position':'YearRep3', 'max':0}, 
									  {'position':'YearRep2', 'max':0}];

				dream['name'] = $(this).attr('data-name');
				dream['pos'] = $(this).attr('data-pos');
				
				$.each(people, function(i, e) {
					if (dream['name'] == e.name && dream['pos'] == e.pos) {
						index = i;
						if ($aClass.hasClass('active') == true)
							dream['count'] = e.count - 1;
						else
							dream['count'] = e.count + 1;
					}
				});

				if (index == -1) {
					dream['count'] = 1;
					people.push(dream);
				} else {
					people[index] = dream;
				}

				
				
				dream = {};
				$(this).toggleClass('active');

				$.each(people, function(i, e) {
					$.each(maxList, function (j, f) {
						if (f.position == e.pos && e.count > f.max) {
							f['candidate'] = e;
							f.max = e.count;
							maxList[j] = f;
						}
					})
				});

				$('.result').html('');
				$('.result2').html('');
				var c = 0;
				$.each(maxList, function(i, e) {
					if (e.candidate) {
						if (c < 5) {
							c += 1;
							$('.result').append(
								'<h4>' + e.candidate.pos + '</h4>' + 
								'<img src="static/img/' + e.candidate.name + '.jpg" class="img-responsive img-rounded" />'
							).hide().fadeIn();
						} else {
							$('.result2').append(
								'<h4>' + e.candidate.pos + '</h4>' + 
								'<img src="static/img/' + e.candidate.name + '.jpg" class="img-responsive img-rounded" />'
							).hide().fadeIn();
						}
					}
				});
			});
		},
		dataType: 'json'
	});

	$(window).scroll(function () {
	    var threshold = 100;
	    if ($(window).scrollTop() >= 100)
	        $('.sidebar').addClass('fixed');
	    else
	        $('.sidebar').removeClass('fixed');
	});

});

