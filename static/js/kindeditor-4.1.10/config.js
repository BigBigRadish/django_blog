KindEditor.ready(function(K) {
                K.create('textarea[name=content]',{
                    width:'800px',
                    height:'200px',
                    uploadJson: '/admin/upload/kindeditor',//配置上传路径在kindediter中
                });
        });