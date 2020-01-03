<?php
$command = escapeshellcmd('python3 Query.py ' . $_POST['banyak'] . ' ' . $_POST['cari']);
$output = shell_exec($command);
$tes=json_decode($output,true);
for($i=0; $i<count($tes); $i++):
   $syntax= shell_exec("cat data/cleaning/".$tes[$i]['doc']);
   $datas = explode("\n",$syntax);
   $tes[$i]['title']=$datas[0];
   $tes[$i]['content']='';
   for ($j=1; $j<count($datas); $j++) { 
      $tes[$i]['content'].=$datas[$j];
   }
endfor;

?>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="author" content="colorlib.com">
  <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500" rel="stylesheet" />
  <link href="template/css/main.css" rel="stylesheet" />

</head>
<body>
  <div class="s002">
    <form action="" method="post">
      <fieldset>
        <legend>SEARCH INFORMATION</legend>
      </fieldset>
      <div class="inner-form">
        <div class="input-field first-wrap">
          <div class="icon-wrap">

          </div>
          <input id="search" name="cari" type="text" placeholder="Find Your Information" />
        </div>
        <div class="input-field fouth-wrap">
          <div class="icon-wrap">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
              <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"></path>
            </svg>
          </div>
          <select data-trigger="" name="banyak">
            <option value="2">2 Article</option>
            <option value="4">4 Article</option>
            <option value="6">6 Article</option>
            <option value="8">8 Article</option>
            <option value="9">9 Article</option>
          </select>
        </div>
        <div class="input-field fifth-wrap">
          <button class="btn-search" type="submit">SEARCH</button>
        </div>
      </div>
    </form>

  <?php foreach($tes as $data):?>
    <div style="background-color: #ffffff; width: 80%;
      margin: auto; border-radius: 10px; justify-content: all; padding: 15px; margin-bottom: 20px;">
      <a href="<?=$data['url']?>"><h3><?=$data['title']?></h3></a>
      <p style="text-align: justify;text-justify: inter-word;">
        <?=$data['content']?>
      </p>
    </div>
  <?php endforeach;?>


</div>


<script src="template/js/extention/choices.js"></script>
<script src="template/js/extention/flatpickr.js"></script>
<script>
  flatpickr(".datepicker",
    {});

  </script>
  <script>
    const choices = new Choices('[data-trigger]',
    {
      searchEnabled: false,
      itemSelectText: '',
    });

  </script>
</body><!-- This templates was made by Colorlib (https://colorlib.com) -->
</html>
