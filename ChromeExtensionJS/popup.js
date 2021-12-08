$(function(){

	console.log('here')
    
    $('#keywordsubmit').click(function(){
		console.log('clicked')
		
		var search_topic = $('#keyword').val();
				
		if (search_topic){
				var url = 'http://127.0.0.1:5000/get/'+ search_topic;
			
				console.log(url);
				
				fetch(url)
				.then(response =>  response.json())
				.then(json => {
					// console.log('parsed json', json) // access json.body here
					json['results'].forEach(element => {
						const split = element['name'].split('##')
						element['timestamp'] = split[0]
						element['courseraLink'] = split[1]
					});
					document.getElementById("p1").innerHTML = "Query: " + json['query'];
					document.getElementById("p2").innerHTML = "Elapsed Time: " + json['elapsed_time'];

					function loadTableData(items) {
						const table = document.getElementById("testBody");
						for(var i = table.rows.length - 1; i >= 0; i--)
						{
							table.deleteRow(i);
						}
						items.forEach( item => {
						  let row = table.insertRow();
						  let content = row.insertCell(0);
						  content.innerHTML = item.content;
						  let timestamp = row.insertCell(1);
						  timestamp.innerHTML = item.timestamp;
						  let courseraLink = row.insertCell(2);
						  courseraLink.innerHTML = item.courseraLink;
						});
					  }
					loadTableData(json['results']);
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