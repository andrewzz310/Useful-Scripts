#!/bin/bash


#clean eip
echo Y | gcloud compute addresses delete kubernetes-the-hard-way


# clean controllers and disk
for i in 0 1 2; do
  echo Y | gcloud compute instances delete controller-${i}
done

# clean worker nodes
for i in 0 1 2; do
  echo Y | gcloud compute instances delete worker-${i} \

done
