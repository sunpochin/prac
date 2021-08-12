

var fs = require('fs');
var express = require('express');
var multer = require('multer')
var app = express();
var upload = multer({ dest: 'upload/' });
var csp = require('express-csp-header');


const { expressCspHeader, INLINE, NONE, SELF } = require('express-csp-header');
 
app.use(expressCspHeader({
    directives: {
//      'unsafe-inline': [NONCE],
        'default-src': [SELF],
        'script-src': [SELF, INLINE, 'somehost.com'],
        'style-src': [SELF, 'mystyles.net'],
        'img-src': ['data:', 'images.com'],
        'worker-src': [NONE],
        'block-all-mixed-content': true
    }
}));


// HTTP response header will be defined as:
// "Content-Security-Policy: default-src 'none'; img-src 'self';"

// 單圖上傳
app.post('/upload-single', upload.single('logo'), function(req, res, next){
   console.log('res: ', res);
   res.send({ret_code: '0'});
});
app.get('/form', function(req, res, next){
   var form = fs.readFileSync('./form.html', {encoding: 'utf8'});
   res.send(form);
});
app.listen(3000);
