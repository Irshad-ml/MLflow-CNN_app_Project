from tensorboard import summary


# model.summary() if we want to print in logs then we can do that by doing logging.info(model.summary()) bcz this return None in the logs  
# So to print the model.summary() into the logs we can create a new .py file and write the below command

import io
import logging

def log_model_summary(model):
    with io.StringIO() as stream:
        model.summary(
            print_fn=lambda x :stream.write(f"{x}\n")
        )
        summary_str=stream.getvalue()
    return summary_str