$(function(){

    
    $('#keywordsubmit').click(function(){
		
		var search_topic = $('#keyword').val();
				
		if (search_topic){
				var url = 'http://127.0.0.1:5000/get/'+ search_topic;
			
				console.log(url);
				
				fetch(url)
				.then(response =>  response.json())
				.then(json => {
					// console.log('parsed json', json) // access json.body here
					document.getElementById("p1").innerHTML = JSON.stringify(json,null, 2);
				})
				.catch(error => console.log(error));

				chrome.runtime.sendMessage(
					{topic: search_topic},
					function(response) {
						result = response.farewell;
						alert(result.summary);
						
						var notifOptions = {
						type: "basic",
						iconUrl: "icon48.png",
						title: "BM25 Search of Your Query",
						message: result.summary
						};
						// console.log(result)
						// document.getElementById("p1").innerHTML = result;
						chrome.notifications.create('WikiNotif', notifOptions);
						
					});
		}
			
			
		$('#keyword').val('');
		
    });
});