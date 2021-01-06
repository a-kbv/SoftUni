<form>
    Names: <input name="names"><br/>
    <input type="submit" value="Send!"/>
</form>
<ul>
<?php
if (isset($_GET['names'])){
    $names = explode(',', $_GET['names']);
    foreach ($names as $index => $name): ?>
    <li><?= $index. " -> ". $name ?></li>
    <?php endforeach;
}
?>
</ul>