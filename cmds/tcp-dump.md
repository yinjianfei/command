        - name: netshoot
          image: nicolaka/netshoot
          command:
          - /bin/sleep
          - infinity
          securityContext:
            capabilities:
              add:         
              - NET_ADMIN
              - NET_RAW



kubectl exec txwl-backend-nginx-5688f48965-jxtwf -nfp -ti -c netshoot -- /bin/bash


tcpdump -i eth0 port 7700