model=$1

for mode in "sync" "synccol" "async" "asynccol"
do
	echo "Training mode $mode"
	if [ $mode = "sync" ] || [ $mode = "async" ]
	then
		hostfile=hosts
	else
		hostfile=hostscol
	fi

	if [ $mode = "sync" ] || [ $mode = "synccol" ]
	then
		kvstore=dist_sync
	else
		kvstore=dist_async
	fi


	for i in 2 4 6 8
	do
		export MXNET_CUDNN_AUTOTUNE_DEFAULT=0
		echo "Hostfile $hostfile$i, kvstore $kvstore"
		echo "Train with $i workers"
		../../tools/launch.py \
			-H $hostfile$i \
			-n $i -s $i \
			--launcher ssh \
			--env "MXNET_CUDNN_AUTOTUNE_DEFAULT" \
			python3.7 image_classification.py \
			--dataset cifar10 \
			--model $model \
			--batch-size 64 \
			--epochs 5 \
			--kvstore $kvstore \
			--gpus "0" | tee $model-log-$mode-$i.txt 
		sleep 5
	done
done
