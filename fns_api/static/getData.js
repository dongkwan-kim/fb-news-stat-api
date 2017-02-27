function getData() {
    return $.ajax({method : 'GET', url:'/static/dummy/dummy_portal.json'})
}
function getPageData() {
    return $.ajax({method : 'GET', url:'/static/dummy/dummy_page.json'})
}
getData().then(function(data){
    app.portals = data;
});
getPageData().then(function(data){
    app.pages = data;  
});
