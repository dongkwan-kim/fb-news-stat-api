var pageNews = {
    props : {
        pages : {}
    },
    data : function() {
        return {
            selectedPages : []
        }
    },
    template : "<div>\
          <div class='row'>\
            <div class='col-md-12 col-sm-12 col-xs-12'>\
                <page-list :pageList='pages'></page-list>\
                <page v-for='page in pages' :page='page' :key='page.pid'></page>\
                <div class='clearfix'></div>\
              </div>\
            </div>\
    </div>"
}

Vue.component('pageNews', pageNews);
