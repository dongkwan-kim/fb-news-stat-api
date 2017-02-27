function getData() {
    var data = {
        "date_from" : "2017-02-21",
        "date_to" : "2017-02-22",
        "token" : "",
        "length" : 5
    }
    return $.ajax({"method": "GET",
                      "url":"/api/v1/portal",
                      "data": data});
}
function getPageData() {
    return $.ajax({method : 'GET', url:'/static/dummy/dummy_page.json'})
}
getData().then(function(data){
    app.portals = JSON.parse(data);
    if ($('#mybarChart').length ){

      var ctx = document.getElementById("mybarChart");
      var mybarChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: [].map.call(app.portals, function(data){return data.name}),
        datasets: [{
          label: '# of news',
          backgroundColor: "#26B99A",
          data: [].map.call(app.portals, function(data){ return data.count })
        }]
      },

      options: {
        scales: {
        yAxes: [{
          ticks: {
          beginAtZero: true
          }
        }]
        }
      }
      });

    }

});
getPageData().then(function(data){
    app.pages = data;
});
