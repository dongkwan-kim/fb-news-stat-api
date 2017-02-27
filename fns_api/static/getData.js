function getData() {
    return $.ajax({method : 'GET', url:'/static/dummy/dummy_portal.json'})
}
function getPageData() {
    return $.ajax({method : 'GET', url:'/static/dummy/dummy_page.json'})
}
getData().then(function(data){
    app.portals = data;
    if ($('#mybarChart').length ){

      var ctx = document.getElementById("mybarChart");
      var mybarChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: [].map.call(app.portals, function(data){return data.name}),
        datasets: [{
          label: '# of Votes',
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
