<?php

require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

function CallPika()
{
    $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
    $channel = $connection->channel();

    $channel->queue_declare('hello', false, false, false, false);

    $msg = new AMQPMessage('Rainy-Weather');
    $channel->basic_publish($msg, '', 'hello');

    echo " [x] Sent 'Rainy-Weather'\n";

    $channel->close();
    $connection->close();
}

function GetPageContents()
{
    $page = file_get_contents('http://127.0.0.1:5000/callClient?temp=12');
    echo $page;
}

// supress a warning with pika.
@CallPika();
GetPageContents();