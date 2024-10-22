
def num_floating_point_operations(args, batch_size):
    if not args.group_query_attention:
        args.num_query_groups = args.num_attention_heads
    return (
        60
        * batch_size
        * args.seq_length
        * args.num_layers
        * args.hidden_size
        * args.hidden_size
        * (
            1
            + (args.num_query_groups / (5 * args.num_attention_heads))
            + (args.seq_length / (5 * args.hidden_size))
            + (args.padded_vocab_size / (10 * args.num_layers * args.hidden_size))
        )
    )