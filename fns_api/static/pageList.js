var pageList = {
  props : {
    pageList : {}
  },
  template : "<div class='col-md-12 col-sm-12 col-xs-12'>\
    <div class='x_panel'>\
      <div class='x_title'>\
        <h2>FaceBook Page Lists</h2>\
        <div class='clearfix'></div>\
      </div>\
      <div class='x_content'>\
        <table id='datatable' class='table table-striped table-bordered'>\
          <thead>\
            <tr>\
              <th>Name</th>\
              <th>Count</th>\
              <th>Link</th>\
              <th>Video</th>\
              <th>None Or Photo</th>\
            </tr>\
          </thead>\
          <tbody>\
            <tr v-for='page in pageList'>\
              <td>{{ page.name }}</td>\
              <td>{{ page.count }}</td>\
              <td>{{ page.ptype.link }}</td>\
              <td>{{ page.ptype.video }}</td>\
              <td>{{ page.ptype.none_or_photo }}</td>\
            </tr>\
          </tbody>\
        </table>\
      </div>\
    </div>\
  </div>\ "
}
Vue.component('pageList', pageList);
