#slightly altered code from   https://github.com/minimaxir/gpt-2-simple
import gpt_2_simple as gpt2
from datetime import datetime
model_name = "124M"
# model is saved into current directory under /models/124M/
#gpt2.download_gpt2(model_name=model_name) #need to run only once. comment out once done.
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)
#gpt2.generate(sess,length=250,
#              temperature=0.7,
#              prefix='Joshua Diao is',
              #prefix='<|startoftext|>',
 #             truncate='<|e',
 #             nsamples=10,
 #             batch_size=10,
              #include_prefix=False
 #             )
gen_file = 'gpt2_gentext.txt'

gpt2.generate_to_file(sess,
              length=250,
              destination_path=gen_file,
              temperature=0.7,
              #prefix='Justin Xiong',
              prefix='<|startoftext|>',
              truncate='<|e',
              nsamples=20,
              batch_size=10,
              include_prefix=False
              )
#files.download(gen_file)
