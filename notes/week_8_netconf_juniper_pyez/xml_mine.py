from lxml import etree


a =
"""
<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<vpn_connection id=\"vpn-02f816e7729d4c7e3\">
<customer_gateway_id>cgw-08b8ee7bbe90e8bda</customer_gateway_id>
<vpn_gateway_id>u003e\u003c</vpn_gateway_id>  
<vpn_connection_type>ipsec.1</vpn_connection_type>
<ipsec_tunnel>
<customer_gateway>
<tunnel_outside_address>
142.103.126.25</tunnel_outside_address>
<tunnel_inside_address>
<ip_address>169.254.177.10</ip_address>
<network_mask>255.255.255.252</network_mask>
<network_cidr>30</network_cidr>
</tunnel_inside_address>
<bgp>
<asn> 65001</asn>
<hold_time>30</hold_time>
</bgp>
</customer_gateway>
<vpn_gateway>
<tunnel_outside_address>
<ip_address>52.60.180.125</ip_address>
</tunnel_outside_address>
<tunnel_inside_address>
<ip_address>169.254.177.9</ip_address>
<network_mask>255.255.255.252</network_mask>
<network_cidr>30</network_cidr>
<tunnel_inside_address>
<bgp>
<asn>64512</asn>
<hold_time>30</hold_time>
</bgp>
<vpn_gateway>
<ike>
<authentication_protocol>sha1</authentication_protocol>
<encryption_protocol>aes-128-cbc</encryption_protocol>
<lifetime>28800</lifetime>
<perfect_forward_secrecy>group2</perfect_forward_secrecy>
<mode>main</mode>
<pre_shared_key>uoAp_DrEd9VMwfygsBfTlyT46GYCpe4_</pre_shared_key>
</ike>
<ipsec>
<protocol>esp</protocol>
<authentication_protocol>hmac-sha1-96</authentication_protocol>
<encryption_protocol>aes-128-cbc</encryption_protocol>
<lifetime>3600</lifetime>
<perfect_forward_secrecy>group2</perfect_forward_secrecy>
<mode>tunnel</mode>
<clear_df_bit>true</clear_df_bit>
<fragmentation_before_encryption>true</fragmentation_before_encryption>
<tcp_mss_adjustment>1379</tcp_mss_adjustment>
<dead_peer_detection>
<interval>10/interval>
<retries>3</retries>
</dead_peer_detection>
</ipsec>
</ipsec_tunnel>
</ipsec_tunnel>
<customer_gateway>
<tunnel_outside_address>
<Ip_address>142.103.126.25</ip_address>
</tunnel_outside_address>
<tunnel_inside_address>
<ip_address>169.254.96.2</ip_address>
<network_mask>255.255.255.252</network_mask>
<network_cidr>30</network_cidr>
</tunnel_inside_address>
<bgp>
<asn>65001</asn>
<hold_time>30</hold_time\>
</bgp>
<customer_gateway>
<vpn_gateway>
<tunnel_outside_address>
<ip_address>52.60.198.117</ip_address>
<tunnel_outside_address>
<Tunnel_inside_address>
<ip_address>169.254.96.1</ip_address>
<network_mask>255.255.255.252</network_mask>
<network_cidr>30</network_cidr>
</tunnel_inside_address>
<bgp>
<asn>64512</asn>
<hold_time>30</hold_time>
</bgp>
</vpn_gateway>
<ike>
<authentication_protocol>sha1</authentication_protocol>
<encryption_protocol>aes-128-cbcu003c/encryption_protocol>
<lifetime>28800</lifetime>
<perfect_forward_secrecy>group2</perfect_forward_secrecy>
<mode>main</mode>
<pre_shared_key>eZhL3BrsUiGPafxYuPAVzBe.qJrhW3h4v</pre_shared_key>
</ike>
<ipsec>
<protocol>esp</protocol>
<authentication_protocol>hmac-sha1-96</authentication_protocol>
<encryption_protocol>aes-128-cbc</encryption_protocol>
<lifetime>3600</lifetime>
<perfect_forward_secrecy>group2</perfect_forward_secrecy>
<mode>tunnel</mode>
<clear_df_bit>true</clear_df_bit>
<fragmentation_before_encryption>true</fragmentation_before_encryption>
<tcp_mss_adjustment>1379</tcp_mss_adjustment>
<dead_peer_detection>
<interval></interval>
<retries>3</retries>
</dead_peer_detection>
<ipsec>
</ipsec_tunnel>
</Vpn_connection>
 
 """"
 
 
 my_xml = etree.fromstring(a)
 Print(etree.tostring(my_xml, encoding="unicode"))