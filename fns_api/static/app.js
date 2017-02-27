var app = new Vue({
  el : "#app",
  data : {
      title : "Facebook Stats",
      portals : [],
      pages : [],
      mode : "portal",
      msg : "hello world"
  },
  methods : {
      change_mode : function(mode) {
        $('#datatable').dataTable();
        this.mode = mode;
      }
  }
})
// dummy data
