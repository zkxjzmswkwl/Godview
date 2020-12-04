var map = null;

function getUsers(callback)
{
	// TODO: change this to a loop
	fetch('http://localhost:5000/ip_to_coords/8.8.8.8,95.173.136.162,202.214.194.147')
		.then((response) => {
			return response.json();
		})
		.then((jsonResponse) => {
			callback(jsonResponse);
		});
}

if (document.getElementById('mapid'))
{
	setTimeout(() => {
		map = L.map('mapid').setView([20.2969, -111.6946], 2);


			L.tileLayer('https://api.maptiler.com/maps/toner/{z}/{x}/{y}.png?key=4TfiqwQswFRo2dgc7GQz', {
				attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>',
			}).addTo(map);

		addUsers();
	}, 500);
	
}

function addUsers (){
	getUsers((data) => {
		console.log(data);
		for (let user in data.results)
		{
			// TODO: Move these to a list. After loop, clean up list, insert new.
			var marker = L.marker([data.results[user].lat, data.results[user].long]).addTo(map);
		}
	});
}
