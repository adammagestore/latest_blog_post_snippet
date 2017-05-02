odoo.define("latest_blog_post_snippet.animation", function(require){
    "use strict";

    var animation = require("web_editor.snippets.animation");

    animation.registry.latest_blog_post_snippet = animation.Class.extend({
        selector: ".oe_latest_blog_post",
        start: function(){
            self = this;
            var number = 3;
            _.each(this.$el.attr('class').split(/\s+/),
                function(cls){
                    if(cls.indexOf('book_snippet-show') == 0){
                        number = parseInt(cls.substring('book_snippet-show'.length));
                    }
                }
            );

            $.get("/snippet/get_latest_blog_post_list", {'number':number}).then(function(data){
                if(data){
                    $(".latest_blog_post_list").replaceWith(data);
                }
            });
        }
    });
});