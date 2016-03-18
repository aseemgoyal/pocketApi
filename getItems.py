import pocket

api = pocket.Api(consumer_key="52621-adc4ebc831cb33231422b620", #"52621-adc4ebc831cb33231422b620",
                 access_token="bd424dd1-a551-c4e1-2959-8054fe") #"2d9adb21-1ff1-bc50-0401-36f0c5")

items_list = api.get()
#print "%d" % (length(items_list))
i=0

for item in items_list:
         i = i+1
         print "%s %s %s %s (%s) %s" % (item.id, item.resolved_id,item.normal_url, item.title, item.resolved_url, ''.join(item.tags))

print i