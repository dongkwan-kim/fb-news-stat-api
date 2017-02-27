var pageNews = {
    props : {
        pages : {}
    },
    template : "<div>\
          <div class='row'>\
            <div class='col-md-12 col-sm-12 col-xs-12'>\
                <page v-for='page in pages' :page='pages' :key='page.pid'></page>\
                <div class='clearfix'></div>\
              </div>\
            </div>\
\
          <br />\
    </div>"
}

Vue.component('pageNews', pageNews);
