# rails/rails

## 8.1.2
- Tag: `v8.1.2`
- Published: 2026-01-08
- URL: https://github.com/rails/rails/releases/tag/v8.1.2

## Active Support

*   Make `delegate` and `delegate_missing_to` work in BasicObject subclasses.

    *Rafael Mendonça França*

*   Fix Inflectors when using a locale that fallbacks to `:en`.

    *Said Kaldybaev*

*   Fix `ActiveSupport::TimeWithZone#as_json` to consistently return UTF-8 strings.

    Previously the returned string would sometime be encoded in US-ASCII, which in
    some cases may be problematic.

    Now the method consistently always return UTF-8 strings.

    *Jean Boussier*

*   Fix `TimeWithZone#xmlschema` when wrapping a `DateTime` instance in local time.

    Previously it would return an invalid time.

    *Dmytro Rymar*

*   Implement LocalCache strategy on `ActiveSupport::Cache::MemoryStore`. The memory store
    needs to respond to the same interface as other cache stores (e.g. `ActiveSupport::NullStore`).

    *Mikey Gough*

*   Fix `ActiveSupport::Inflector.humanize` with international characters.

    ```ruby
    ActiveSupport::Inflector.humanize("áÉÍÓÚ")  # => "Áéíóú"
    ActiveSupport::Inflector.humanize("аБВГДЕ") # => "Абвгде"
    ```

    *Jose Luis Duran*


## Active Model

*   No changes.


## Active Record

*   Fix counting cached queries in `ActiveRecord::RuntimeRegistry`.

    *fatkodima*

*   Fix merging relations with arel equality predicates with null relations.

    *fatkodima*

*   Fix SQLite3 schema dump for non-autoincrement integer primary keys.

    Previously, `schema.rb` should incorrectly restore that table with an auto incrementing
    primary key.

    *Chris Hasiński*

*   Fix PostgreSQL `schema_search_path` not being reapplied after `reset!` or `reconnect!`.

    The `schema_search_path` configured in `database.yml` is now correctly
    reapplied instead of falling back to PostgreSQL defaults.

    *Tobias Egli*

*   Restore the ability of enum to be foats.

    ```ruby
    enum :rating, { low: 0.0, medium: 0.5, high: 1.0 },
    ```

    In Rails 8.1.0, enum values are eagerly validated, and floats weren't expected.

    *Said Kaldybaev*

*   Ensure batched preloaded associations accounts for klass when grouping to avoid issues with STI.

    *zzak*, *Stjepan Hadjic*

*   Fix `ActiveRecord::SoleRecordExceeded#record` to return the relation.

    This was the case until Rails 7.2, but starting from 8.0 it
    started mistakenly returning the model class.

    *Jean Boussier*

*   Improve PostgreSQLAdapter resilience to Timeout.timeout.

    Better handle asynchronous exceptions being thrown inside
    the `reconnect!` method.

    This may fixes some deep errors such as:

    ```
    undefined method `key?' for nil:NilClass (NoMethodError)
              if !type_map.key?(oid)
    ```

    *Jean Boussier*

*   Fix structured events for Active Record was not being emitted.

    *Yuji Yaginuma*

*   Fix `eager_load` when loading `has_many` assocations with composite primary keys.

    This would result in some records being loaded multiple times.

    *Martin-Alexander*


## Action View

*   Fix `file_field` to join mime types with a comma when provided as Array

    ```ruby
    file_field(:article, :image, accept: ['image/png', 'image/gif', 'image/jpeg'])
    ```

    Now behaves likes:

    ```
    file_field(:article, :image, accept: 'image/png,image/gif,image/jpeg')
    ```

    *Bogdan Gusiev*

*   Fix strict locals parsing to handle multiline definitions.

    *Said Kaldybaev*

*   Fix `content_security_policy_nonce` error in mailers when using `content_security_policy_nonce_auto` setting.

    The `content_security_policy_nonce helper` is provided by `ActionController::ContentSecurityPolicy`, and it relies on `request.content_security_policy_nonc`e. Mailers lack both the module and the request object.

    *Jarrett Lusso*


## Action Pack

*   Add `config.action_controller.live_streaming_excluded_keys` to control execution state sharing in ActionController::Live.

    When using ActionController::Live, actions are executed in a separate thread that shares
    state from the parent thread. This new configuration allows applications to opt-out specific
    state keys that should not be shared.

    This is useful when streaming inside a `connected_to` block, where you may want
    the streaming thread to use its own database connection context.

    ```ruby
    # config/application.rb
    config.action_controller.live_streaming_excluded_keys = [:active_record_connected_to_stack]
    ```

    By default, all keys are shared.

    *Eileen M. Uchitelle*

*   Fix `IpSpoofAttackError` message to include `Forwarded` header content.

    Without it, the error message may be misleading.

    *zzak*


## Active Job

*   Fix `ActiveJob.perform_all_later` to respect `job_class.enqueue_after_transaction_commit`.

    Previously, `perform_all_later` would enqueue all jobs immediately, even if
    they had `enqueue_after_transaction_commit = true`. Now it correctly defers
    jobs with this setting until after transaction commits, matching the behavior
    of `perform_later`.

    *OuYangJinTing*

*   Fix using custom serializers with `ActiveJob::Arguments.serialize` when
    `ActiveJob::Base` hasn't been loaded.

    *Hartley McGuire*

## Action Mailer

*   No changes.


## Action Cable

*   No changes.


## Active Storage

*   Restore ADC when signing URLs with IAM for GCS

    ADC was previously used for automatic authorization when signing URLs with IAM.
    Now it is again, but the auth client is memoized so that new credentials are only
    requested when the current ones expire. Other auth methods can now be used
    instead by setting the authorization on `ActiveStorage::Service::GCSService#iam_client`.

    ```ruby
    ActiveStorage::Blob.service.iam_client.authorization = Google::Auth::ImpersonatedServiceAccountCredentials.new(options)
    ```

    This is safer than setting `Google::Apis::RequestOptions.default.authorization`
    because it only applies to Active Storage and does not affect other Google API
    clients.

    *Justin Malčić*


## Action Mailbox

*   No changes.


## Action Text

*   No changes.


## Railties

*   Skip all system test files on app generation.

    *Eileen M. Uchitelle*

*   Fix `db:system:change` to correctly update Dockerfile base packages.

    *Josiah Smith*

*   Fix devcontainer volume mount when app name differs from folder name.

    *Rafael Mendonça França*

*   Fixed the `rails notes` command to properly extract notes in CSS files.

    *David White*

*   Fixed the default Dockerfile to properly include the `vendor/` directory during `bundle install`.

    *Zhong Sheng*


## Guides

*   No changes.

## 8.1.1
- Tag: `v8.1.1`
- Published: 2025-10-28
- URL: https://github.com/rails/rails/releases/tag/v8.1.1

## Active Support

*   No changes.


## Active Model

*   No changes.


## Active Record

*   No changes.


## Action View

*   Respect `remove_hidden_field_autocomplete` config in form builder `hidden_field`.

    *Rafael Mendonça França*


## Action Pack

*   Allow methods starting with underscore to be action methods.

    Disallowing methods starting with an underscore from being action methods
    was an unintended side effect of the performance optimization in
    207a254.

    Fixes #55985.

    *Rafael Mendonça França*


## Active Job

*   Only index new serializers.

    *Jesse Sharps*


## Action Mailer

*   No changes.


## Action Cable

*   No changes.


## Active Storage

*   No changes.


## Action Mailbox

*   No changes.


## Action Text

*   No changes.


## Railties

*   Do not assume and force SSL in production by default when using Kamal, to allow for out of the box Kamal deployments.

    It is still recommended to assume and force SSL in production as soon as you can.

    *Jerome Dalbert*

## Guides

*   No changes.

## 8.0.4
- Tag: `v8.0.4`
- Published: 2025-10-28
- URL: https://github.com/rails/rails/releases/tag/v8.0.4

## Active Support

*   Fix `Enumerable#sole` to return the full tuple instead of just the first element of the tuple.

    *Olivier Bellone*

*   Fix parallel tests hanging when worker processes die abruptly.

    Previously, if a worker process was killed (e.g., OOM killed, `kill -9`) during parallel
    test execution, the test suite would hang forever waiting for the dead worker.

    *Joshua Young*

*   Fix `NameError` when `class_attribute` is defined on instance singleton classes.

    Previously, calling `class_attribute` on an instance's singleton class would raise
    a `NameError` when accessing the attribute through the instance.

    ```ruby
    object = MyClass.new
    object.singleton_class.class_attribute :foo, default: "bar"
    object.foo # previously raised NameError, now returns "bar"
    ```

    *Joshua Young*


## Active Model

*   No changes.


## Active Record

*   Fix SQLite3 data loss during table alterations with CASCADE foreign keys.

    When altering a table in SQLite3 that is referenced by child tables with
    `ON DELETE CASCADE` foreign keys, ActiveRecord would silently delete all
    data from the child tables. This occurred because SQLite requires table
    recreation for schema changes, and during this process the original table
    is temporarily dropped, triggering CASCADE deletes on child tables.

    The root cause was incorrect ordering of operations. The original code
    wrapped `disable_referential_integrity` inside a transaction, but
    `PRAGMA foreign_keys` cannot be modified inside a transaction in SQLite -
    attempting to do so simply has no effect. This meant foreign keys remained
    enabled during table recreation, causing CASCADE deletes to fire.

    The fix reverses the order to follow the official SQLite 12-step ALTER TABLE
    procedure: `disable_referential_integrity` now wraps the transaction instead
    of being wrapped by it. This ensures foreign keys are properly disabled
    before the transaction starts and re-enabled after it commits, preventing
    CASCADE deletes while maintaining data integrity through atomic transactions.

    *Ruy Rocha*

*   Add support for bound SQL literals in CTEs.

    *Nicolas Bachschmidt*

*   Fix `belongs_to` associations not to clear the entire composite primary key.

    When clearing a `belongs_to` association that references a model with composite primary key,
    only the optional part of the key should be cleared.

    *zzak*

*   Fix invalid records being autosaved when distantly associated records are marked for deletion.

    *Ian Terrell*, *axlekb AB*


## Action View

*   Restore `add_default_name_and_id` method.

    *Hartley McGuire*


## Action Pack

*   Submit test requests using `as: :html` with `Content-Type: x-www-form-urlencoded`

    *Sean Doyle*


## Active Job

*   No changes.


## Action Mailer

*   No changes.


## Action Cable

*   No changes.


## Active Storage

*   No changes.


## Action Mailbox

*   No changes.


## Action Text

*   No changes.


## Railties

*   No changes.


## Guides

*   No changes.

## 7.2.3
- Tag: `v7.2.3`
- Published: 2025-10-28
- URL: https://github.com/rails/rails/releases/tag/v7.2.3

## Active Support

*   Fix `Enumerable#sole` to return the full tuple instead of just the first element of the tuple.

    *Olivier Bellone*

*   Fix parallel tests hanging when worker processes die abruptly.

    Previously, if a worker process was killed (e.g., OOM killed, `kill -9`) during parallel
    test execution, the test suite would hang forever waiting for the dead worker.

    *Joshua Young*

*   `ActiveSupport::FileUpdateChecker` does not depend on `Time.now` to prevent unnecessary reloads with time travel test helpers

    *Jan Grodowski*

*   Fix `ActiveSupport::BroadcastLogger` from executing a block argument for each logger (tagged, info, etc.).

    *Jared Armstrong*

*   Fix `ActiveSupport::HashWithIndifferentAccess#transform_keys!` removing defaults.

    *Hartley McGuire*

*   Fix `ActiveSupport::HashWithIndifferentAccess#tranform_keys!` to handle collisions.

    If the transformation would result in a key equal to another not yet transformed one,
    it would result in keys being lost.

    Before:

    ```ruby
    >> {a: 1, b: 2}.with_indifferent_access.transform_keys!(&:succ)
    => {"c" => 1}
    ```

    After:

    ```ruby
    >> {a: 1, b: 2}.with_indifferent_access.transform_keys!(&:succ)
    => {"c" => 1, "d" => 2}
    ```

    *Jason T Johnson*, *Jean Boussier*

*   Fix `ActiveSupport::Cache::MemCacheStore#read_multi` to handle network errors.

    This method specifically wasn't handling network errors like other codepaths.

    *Alessandro Dal Grande*

*   Fix Active Support Cache `fetch_multi` when local store is active.

    `fetch_multi` now properly yield to the provided block for missing entries
    that have been recorded as such in the local store.

    *Jean Boussier*

*   Fix execution wrapping to report all exceptions, including `Exception`.

    If a more serious error like `SystemStackError` or `NoMemoryError` happens,
    the error reporter should be able to report these kinds of exceptions.

    *Gannon McGibbon*

*   Fix `RedisCacheStore` and `MemCacheStore` to also handle connection pool related errors.

    These errors are rescued and reported to `Rails.error`.

    *Jean Boussier*

*   Fix `ActiveSupport::Cache#read_multi` to respect version expiry when using local cache.

    *zzak*

*   Fix `ActiveSupport::MessageVerifier` and `ActiveSupport::MessageEncryptor` configuration of `on_rotation` callback.

    ```ruby
    verifier.rotate(old_secret).on_rotation { ... }
    ```

    Now both work as documented.

    *Jean Boussier*

*   Fix `ActiveSupport::MessageVerifier` to always be able to verify both URL-safe and URL-unsafe payloads.

    This is to allow transitioning seemlessly from either configuration without immediately invalidating
    all previously generated signed messages.

    *Jean Boussier*, *Florent Beaurain*, *Ali Sepehri*

*   Fix `cache.fetch` to honor the provided expiry when `:race_condition_ttl` is used.

    ```ruby
    cache.fetch("key", expires_in: 1.hour, race_condition_ttl: 5.second) do
      "something"
    end
    ```

    In the above example, the final cache entry would have a 10 seconds TTL instead
    of the requested 1 hour.

    *Dhia*

*   Better handle procs with splat arguments in `set_callback`.

    *Radamés Roriz*

*   Fix `String#mb_chars` to not mutate the receiver.

    Previously it would call `force_encoding` on the receiver,
    now it dups the receiver first.

    *Jean Boussier*

*   Improve `ErrorSubscriber` to also mark error causes as reported.

    This avoid some cases of errors being reported twice, notably in views because of how
    errors are wrapped in `ActionView::Template::Error`.

    *Jean Boussier*

*   Fix `Module#module_parent_name` to return the correct name after the module has been named.

    When called on an anonymous module, the return value wouldn't change after the module was given a name
    later by being assigned to a constant.

    ```ruby
    mod = Module.new
    mod.module_parent_name # => "Object"
    MyModule::Something = mod
    mod.module_parent_name # => "MyModule"
    ```

    *Jean Boussier*

*   Fix a bug in `ERB::Util.tokenize` that causes incorrect tokenization when ERB tags are preceeded by multibyte characters.

    *Martin Emde*


## Active Model

*   Fix `has_secure_password` to perform confirmation validation of the password even when blank.

    The validation was incorrectly skipped when the password only contained whitespace characters.

    *Fabio Sangiovanni*

*   Handle missing attributes for `ActiveModel::Translation#human_attribute_name`.

    *zzak*

*   Fix `ActiveModel::AttributeAssignment#assign_attributes` to accept objects without `each`.

    *Kouhei Yanagita*


## Active Record

*   Fix SQLite3 data loss during table alterations with CASCADE foreign keys.

    When altering a table in SQLite3 that is referenced by child tables with
    `ON DELETE CASCADE` foreign keys, ActiveRecord would silently delete all
    data from the child tables. This occurred because SQLite requires table
    recreation for schema changes, and during this process the original table
    is temporarily dropped, triggering CASCADE deletes on child tables.

    The root cause was incorrect ordering of operations. The original code
    wrapped `disable_referential_integrity` inside a transaction, but
    `PRAGMA foreign_keys` cannot be modified inside a transaction in SQLite -
    attempting to do so simply has no effect. This meant foreign keys remained
    enabled during table recreation, causing CASCADE deletes to fire.

    The fix reverses the order to follow the official SQLite 12-step ALTER TABLE
    procedure: `disable_referential_integrity` now wraps the transaction instead
    of being wrapped by it. This ensures foreign keys are properly disabled
    before the transaction starts and re-enabled after it commits, preventing
    CASCADE deletes while maintaining data integrity through atomic transactions.

    *Ruy Rocha*

*   Fix `belongs_to` associations not to clear the entire composite primary key.

    When clearing a `belongs_to` association that references a model with composite primary key,
    only the optional part of the key should be cleared.

    *zzak*

*   Fix invalid records being autosaved when distantly associated records are marked for deletion.

    *Ian Terrell*, *axlekb AB*

*   Prevent persisting invalid record.

    *Edouard Chin*

*   Fix count with group by qualified name on loaded relation.

    *Ryuta Kamizono*

*   Fix `sum` with qualified name on loaded relation.

    *Chris Gunther*

*   Fix prepared statements on mysql2 adapter.

    *Jean Boussier*

*   Fix query cache for pinned connections in multi threaded transactional tests.

    When a pinned connection is used across separate threads, they now use a separate cache store
    for each thread.

    This improve accuracy of system tests, and any test using multiple threads.

    *Heinrich Lee Yu*, *Jean Boussier*

*   Don't add `id_value` attribute alias when attribute/column with that name already exists.

    *Rob Lewis*

*   Fix false positive change detection involving STI and polymorhic has one relationships.

    Polymorphic `has_one` relationships would always be considered changed when defined in a STI child
    class, causing nedless extra autosaves.

    *David Fritsch*

*   Fix stale associaton detection for polymophic `belong_to`.

    *Florent Beaurain*, *Thomas Crambert*

*   Fix removal of PostgreSQL version comments in `structure.sql` for latest PostgreSQL versions which include `\restrict`.

    *Brendan Weibrecht*

*   Fix `#merge` with `#or` or `#and` and a mixture of attributes and SQL strings resulting in an incorrect query.

    ```ruby
    base = Comment.joins(:post).where(user_id: 1).where("recent = 1")
    puts base.merge(base.where(draft: true).or(Post.where(archived: true))).to_sql
    ```

    Before:

    ```SQL
    SELECT "comments".* FROM "comments"
    INNER JOIN "posts" ON "posts"."id" = "comments"."post_id"
    WHERE (recent = 1)
    AND (
      "comments"."user_id" = 1
      AND (recent = 1)
      AND "comments"."draft" = 1
      OR "posts"."archived" = 1
    )
    ```

    After:

    ```SQL
    SELECT "comments".* FROM "comments"
    INNER JOIN "posts" ON "posts"."id" = "comments"."post_id"
    WHERE "comments"."user_id" = 1
    AND (recent = 1)
    AND (
      "comments"."user_id" = 1
      AND (recent = 1)
      AND "comments"."draft" = 1
      OR "posts"."archived" = 1
    )
    ```

    *Joshua Young*

*   Fix inline `has_and_belongs_to_many` fixtures for tables with composite primary keys.

    *fatkodima*

*   Fix `annotate` comments to propagate to `update_all`/`delete_all`.

    *fatkodima*

*   Fix checking whether an unpersisted record is `include?`d in a strictly
    loaded `has_and_belongs_to_many` association.

    *Hartley McGuire*

*   Fix inline has_and_belongs_to_many fixtures for tables with composite primary keys.

    *fatkodima*

*   `create_or_find_by` will now correctly rollback a transaction.

    When using `create_or_find_by`, raising a ActiveRecord::Rollback error
    in a `after_save` callback had no effect, the transaction was committed
    and a record created.

    *Edouard Chin*

*   Gracefully handle `Timeout.timeout` firing during connection configuration.

    Use of `Timeout.timeout` could result in improperly initialized database connection.

    This could lead to a partially configured connection being used, resulting in various exceptions,
    the most common being with the PostgreSQLAdapter raising `undefined method 'key?' for nil`
    or `TypeError: wrong argument type nil (expected PG::TypeMap)`.

    *Jean Boussier*

*   The SQLite3 adapter quotes non-finite Numeric values like "Infinity" and "NaN".

    *Mike Dalessio*

*   Handle libpq returning a database version of 0 on no/bad connection in `PostgreSQLAdapter`.

    Before, this version would be cached and an error would be raised during connection configuration when
    comparing it with the minimum required version for the adapter. This meant that the connection could
    never be successfully configured on subsequent reconnection attempts.

    Now, this is treated as a connection failure consistent with libpq, raising a `ActiveRecord::ConnectionFailed`
    and ensuring the version isn't cached, which allows the version to be retrieved on the next connection attempt.

    *Joshua Young*, *Rian McGuire*

*   Fix error handling during connection configuration.

    Active Record wasn't properly handling errors during the connection configuration phase.
    This could lead to a partially configured connection being used, resulting in various exceptions,
    the most common being with the PostgreSQLAdapter raising `undefined method `key?' for nil`
    or `TypeError: wrong argument type nil (expected PG::TypeMap)`.

    *Jean Boussier*

*   Fix a case where a non-retryable query could be marked retryable.

    *Hartley McGuire*

*   Handle circular references when autosaving associations.

    *zzak*

*   Prevent persisting invalid record.

    *Edouard Chin*

*   Fix support for PostgreSQL enum types with commas in their name.

    *Arthur Hess*

*   Fix inserts on MySQL with no RETURNING support for a table with multiple auto populated columns.

    *Nikita Vasilevsky*

*   Fix joining on a scoped association with string joins and bind parameters.

    ```ruby
    class Instructor < ActiveRecord::Base
      has_many :instructor_roles, -> { active }
    end

    class InstructorRole < ActiveRecord::Base
      scope :active, -> {
        joins("JOIN students ON instructor_roles.student_id = students.id")
        .where(students { status: 1 })
      }
    end

    Instructor.joins(:instructor_roles).first
    ```

    The above example would result in `ActiveRecord::StatementInvalid` because the
    `active` scope bind parameters would be lost.

    *Jean Boussier*

*   Fix a potential race condition with system tests and transactional fixtures.

    *Sjoerd Lagarde*

*   Fix count with group by qualified name on loaded relation.

    *Ryuta Kamizono*

*   Fix sum with qualified name on loaded relation.

    *Chris Gunther*

*   Fix autosave associations to no longer validated unmodified associated records.

    Active Record was incorrectly performing validation on associated record that
    weren't created nor modified as part of the transaction:

    ```ruby
    Post.create!(author: User.find(1)) # Fail if user is invalid
    ```

    *Jean Boussier*

*   Remember when a database connection has recently been verified (for
    two seconds, by default), to avoid repeated reverifications during a
    single request.

    This should recreate a similar rate of verification as in Rails 7.1,
    where connections are leased for the duration of a request, and thus
    only verified once.

    *Matthew Draper*

*   Fix prepared statements on mysql2 adapter.

    *Jean Boussier*

*   Fix a race condition in `ActiveRecord::Base#method_missing` when lazily defining attributes.

    If multiple thread were concurrently triggering attribute definition on the same model,
    it could result in a `NoMethodError` being raised.

    *Jean Boussier*

*   Fix MySQL default functions getting dropped when changing a column's nullability.

    *Bastian Bartmann*

*   Fix `add_unique_constraint`/`add_check_constraint`/`/`add_foreign_key` to be revertible when
    given invalid options.

    *fatkodima*

*   Fix asynchronous destroying of polymorphic `belongs_to` associations.

    *fatkodima*

*   NOT VALID constraints should not dump in `create_table`.

    *Ryuta Kamizono*

*   Fix finding by nil composite primary key association.

    *fatkodima*

*   Fix parsing of SQLite foreign key names when they contain non-ASCII characters

    *Zacharias Knudsen*

*   Fix parsing of MySQL 8.0.16+ CHECK constraints when they contain new lines.

    *Steve Hill*

*   Ensure normalized attribute queries use `IS NULL` consistently for `nil` and normalized `nil` values.

    *Joshua Young*

*   Restore back the ability to pass only database name for `DATABASE_URL`.

    *fatkodima*

*   Fix `order` with using association name as an alias.

    *Ryuta Kamizono*

*   Improve invalid argument error for with.

    *Ryuta Kamizono*

*   Deduplicate `with` CTE expressions.

    *fatkodima*


## Action View

*   Fix `javascript_include_tag` `type` option to accept either strings and symbols.

    ```ruby
    javascript_include_tag "application", type: :module
    javascript_include_tag "application", type: "module"
    ```

    Previously, only the string value was recoginized.

    *Jean Boussier*

*   Fix `excerpt` helper with non-whitespace separator.

    *Jonathan Hefner*

*   Respect `html_options[:form]` when `collection_checkboxes` generates the
    hidden `<input>`.

    *Riccardo Odone*

*   Layouts have access to local variables passed to `render`.

    This fixes #31680 which was a regression in Rails 5.1.

    *Mike Dalessio*

*   Argument errors related to strict locals in templates now raise an
    `ActionView::StrictLocalsError`, and all other argument errors are reraised as-is.

    Previously, any `ArgumentError` raised during template rendering was swallowed during strict
    local error handling, so that an `ArgumentError` unrelated to strict locals (e.g., a helper
    method invoked with incorrect arguments) would be replaced by a similar `ArgumentError` with an
    unrelated backtrace, making it difficult to debug templates.

    Now, any `ArgumentError` unrelated to strict locals is reraised, preserving the original
    backtrace for developers.

    Also note that `ActionView::StrictLocalsError` is a subclass of `ArgumentError`, so any existing
    code that rescues `ArgumentError` will continue to work.

    Fixes #52227.

    *Mike Dalessio*

*   Fix stack overflow error in dependency tracker when dealing with circular dependencies

    *Jean Boussier*

*   Fix a crash in ERB template error highlighting when the error occurs on a
    line in the compiled template that is past the end of the source template.

    *Martin Emde*

*   Improve reliability of ERB template error highlighting.
    Fix infinite loops and crashes in highlighting and
    improve tolerance for alternate ERB handlers.

    *Martin Emde*


## Action Pack

*   Submit test requests using `as: :html` with `Content-Type: x-www-form-urlencoded`

    *Sean Doyle*

*   Address `rack 3.2` deprecations warnings.

    ```
    warning: Status code :unprocessable_entity is deprecated and will be removed in a future version of Rack.
    Please use :unprocessable_content instead.
    ```

    Rails API will transparently convert one into the other for the forseable future.

    *Earlopain*, *Jean Boussier*

*   Always return empty body for HEAD requests in `PublicExceptions` and
    `DebugExceptions`.

    This is required by `Rack::Lint` (per RFC9110).

    *Hartley McGuire*

*   Fix `url_for` to handle `:path_params` gracefully when it's not a `Hash`.

    Prevents various security scanners from causing exceptions.

    *Martin Emde*

*   Fix `ActionDispatch::Executor` to unwrap exceptions like other error reporting middlewares.

    *Jean Boussier*

*   Fix NoMethodError when a non-string CSRF token is passed through headers.

    *Ryan Heneise*

*   Fix invalid response when rescuing `ActionController::Redirecting::UnsafeRedirectError` in a controller.

    *Alex Ghiculescu*


## Active Job

*   Include the actual Active Job locale when serializing rather than I18n locale.

    *Adrien S*

*   Avoid crashing in Active Job logger when logging enqueueing errors

    `ActiveJob.perform_all_later` could fail with a `TypeError` when all
    provided jobs failed to be enqueueed.

    *Efstathios Stivaros*


## Action Mailer

*   No changes.


## Action Cable

*   Fixed compatibility with `redis` gem `5.4.1`

    *Jean Boussier*

*   Fixed a possible race condition in `stream_from`.

    *OuYangJinTing*

*   Ensure the Postgresql adapter always use a dedicated connection even during system tests.

    Fix an issue with the Action Cable Postgresql adapter causing deadlock or various weird
    pg client error during system tests.

    *Jean Boussier*


## Active Storage

*   Fix `config.active_storage.touch_attachment_records` to work with eager loading.

    *fatkodima*

*   A Blob will no longer autosave associated Attachment.

    This fixes an issue where a record with an attachment would have
    its dirty attributes reset, preventing your `after commit` callbacks
    on that record to behave as expected.

    Note that this change doesn't require any changes on your application
    and is supposed to be internal. Active Storage Attachment will continue
    to be autosaved (through a different relation).

    *Edouard-chin*


## Action Mailbox

*   No changes.


## Action Text

*   No changes.


## Railties

*   Use `secret_key_base` from ENV or credentials when present locally.

    When ENV["SECRET_KEY_BASE"] or
    `Rails.application.credentials.secret_key_base` is set for test or
    development, it is used for the `Rails.config.secret_key_base`,
    instead of generating a `tmp/local_secret.txt` file.

    *Petrik de Heus*


## Guides

*   No changes.

## 7.1.6
- Tag: `v7.1.6`
- Published: 2025-10-28
- URL: https://github.com/rails/rails/releases/tag/v7.1.6

## Active Support

*   No changes.


## Active Model

*   No changes.


## Active Record

*   Gracefully handle `Timeout.timeout` firing during connection configuration.

    Use of `Timeout.timeout` could result in improperly initialized database connection.

    This could lead to a partially configured connection being used, resulting in various exceptions,
    the most common being with the PostgreSQLAdapter raising `undefined method `key?' for nil`
    or `TypeError: wrong argument type nil (expected PG::TypeMap)`.

    *Jean Boussier*

*   Fix error handling during connection configuration.

    Active Record wasn't properly handling errors during the connection configuration phase.
    This could lead to a partially configured connection being used, resulting in various exceptions,
    the most common being with the PostgreSQLAdapter raising `undefined method `key?' for nil`
    or `TypeError: wrong argument type nil (expected PG::TypeMap)`.

    *Jean Boussier*

*   Fix prepared statements on mysql2 adapter.

    *Jean Boussier*

*   Fix a race condition in `ActiveRecord::Base#method_missing` when lazily defining attributes.

    If multiple thread were concurrently triggering attribute definition on the same model,
    it could result in a `NoMethodError` being raised.

    *Jean Boussier*


## Action View

*   No changes.


## Action Pack

*   No changes.


## Active Job

*   No changes.


## Action Mailer

*   No changes.


## Action Cable

*   Fixed compatibility with `redis` gem `5.4.1`

    *Jean Boussier*


## Active Storage

*   No changes.


## Action Mailbox

*   No changes.


## Action Text

*   No changes.


## Railties

*   No changes.


## Guides

*   No changes.

## 7.0.10
- Tag: `v7.0.10`
- Published: 2025-10-28
- URL: https://github.com/rails/rails/releases/tag/v7.0.10

See https://github.com/rails/rails/releases/tag/v7.0.9 for information about this release.

## 7.0.9
- Tag: `v7.0.9`
- Published: 2025-10-28
- URL: https://github.com/rails/rails/releases/tag/v7.0.9

## Active Support

*   Fix `ActiveSupport::Notifications.publish_event` to preserve units.

    This solves the incorrect reporting of time spent running Active Record
    asynchronous queries (by a factor `1000`).

    *Jean Boussier*

*   Fix ActiveSupport::Deprecation to handle blaming generated code

    *Jean Boussier*, *fatkodima*

*   Fix `#to_fs(:human_size)` to correctly work with negative numbers.

    *Earlopain*

*   Add `bigdecimal` as Active Support dependency that is a bundled gem candidate for Ruby 3.4.

    `bigdecimal` 3.1.4 or higher version will be installed.
    Ruby 2.7 and 3.0 users who want `bigdecimal` version 2.0.0 or 3.0.0 behavior as a default gem,
    pin the `bigdecimal` version in your application Gemfile.

    *Koichi ITO*

*   Ensure `{down,up}case_first` returns non-frozen string.

    *Jonathan Hefner*

*   Add `drb`, `mutex_m` and `base64` that are bundled gem candidates for Ruby 3.4

    *Yasuo Honda*

*   Fix `delete_matched` for file cache store to work with keys longer than the
    max filename size.

    *fatkodima* and *Jonathan Hefner*

*   Fix MemoryStore to prevent race conditions when incrementing or decrementing.

    *Pierre Jambet*

*   Fix MemoryStore to preserve entries TTL when incrementing or decrementing

    This is to be more consistent with how MemCachedStore and RedisCacheStore behaves.

    *Jean Boussier*

*   NumberHelper: handle objects responding to_d.

    *fatkodima*

*   NumberHelper: handle very large numbers.

    *Alex Ghiculescu*, *fatkodima*

*   Fix Range#overlaps? not taking empty ranges into account on Ruby < 3.3

    *Nobuyoshi Nakada*, *Shouichi Kamiya*, *Hartley McGuire*


## Active Model

*   No changes.


## Active Record

*   Fix an issue that could cause database connection leaks

    If Active Record successfully connected to the database, but then failed
    to read the server informations, the connection would be leaked until the
    Ruby garbage collector triggers.

    *Jean Boussier*

*   Fix single quote escapes on default generated MySQL columns

    MySQL 5.7.5+ supports generated columns, which can be used to create a column that is computed from an expression.

    Previously, the schema dump would output a string with double escapes for generated columns with single quotes in the default expression.

    This would result in issues when importing the schema on a fresh instance of a MySQL database.

    Now, the string will not be escaped and will be valid Ruby upon importing of the schema.

    *Yash Kapadia*

*   Fix `Relation#transaction` to not apply a default scope

    The method was incorrectly setting a default scope around its block:

    ```ruby
    Post.where(published: true).transaction do
      Post.count # SELECT COUNT(*) FROM posts WHERE published = FALSE;
    end
    ```

    *Jean Boussier*

*   Fix renaming primary key index when renaming a table with a UUID primary key
    in PostgreSQL.

    *fatkodima*

*   Fix `where(field: values)` queries when `field` is a serialized attribute
    (for example, when `field` uses `ActiveRecord::Base.serialize` or is a JSON
    column).

    *João Alves*

*   Don't mark Float::INFINITY as changed when reassigning it

    When saving a record with a float infinite value, it shouldn't mark as changed

    *Maicol Bentancor*

*   `ActiveRecord::Base.table_name` now returns `nil` instead of raising
    "undefined method `abstract_class?` for Object:Class".

    *a5-stable*

*   Fix upserting for custom `:on_duplicate` and `:unique_by` consisting of all
    inserts keys.

    *fatkodima*

*   Fix `NoMethodError` when casting a PostgreSQL `money` value that uses a
    comma as its radix point and has no leading currency symbol.  For example,
    when casting `"3,50"`.

    *Andreas Reischuck* and *Jonathan Hefner*

*   Fix duplicate quoting for check constraint expressions in schema dump when using MySQL

    A check constraint with an expression, that already contains quotes, lead to an invalid schema
    dump with the mysql2 adapter.

    Fixes #42424.

    *Felix Tscheulin*

*   Fix MySQL expression index dumping with escaped quotes.

    *fatkodima*

*   Fix uniqueness validation on association not using overridden primary key.

    *fatkodima*


## Action View

*   Fix the `number_to_human_size` view helper to correctly work with negative numbers.

    *Earlopain*


## Action Pack

*   Fix `ActionDispatch::Executor` middleware to report errors handled by `ActionDispatch::ShowExceptions`.

    In the default production environment, `ShowExceptions` rescue uncaught errors
    and returns a response. Because if this the executor wouldn't report production
    errors with the default Rails configuration.

    *Jean Boussier*

*   Add `racc` as a dependency since it will become a bundled gem in Ruby 3.4.0

    *Hartley McGuire*


## Active Job

*   Preserve the serialized timezone when deserializing `ActiveSupport::TimeWithZone` arguments.

    *Joshua Young*


## Action Mailer

*   No changes.


## Action Cable

*   No changes.


## Active Storage

*   Fix `ActiveStorage::Representations::ProxyController` not returning the proper
    preview image variant for previewable files.

    *Chedli Bourguiba*

*   Make untracked variants obey `config.active_storage.content_types_to_serve_as_binary`
    and `config.active_storage.content_types_allowed_inline`.

    *Chedli Bourguiba* and *Jonathan Hefner*

*   Fix direct upload forms when submit button contains nested elements.

    *Marc Köhlbrugge*

*   Prevent `ActiveRecord::StrictLoadingViolationError` when strict loading is
    enabled and the variant of an Active Storage preview has already been
    processed (for example, by calling `ActiveStorage::Preview#url`).

    *Jonathan Hefner*

*   Fix variants not included when eager loading multiple records containing a single attachment

    When using the `with_attached_#{name}` scope for a `has_one_attached` relation,
    attachment variants were not eagerly loaded.

    *Russell Porter*


## Action Mailbox

*   No changes.


## Action Text

*   No changes.


## Railties

*   No changes.


## Guides

*   No changes.

## 8.1.0
- Tag: `v8.1.0`
- Published: 2025-10-22
- URL: https://github.com/rails/rails/releases/tag/v8.1.0

## Active Support

*   Remove deprecated passing a Time object to `Time#since`.

    *Rafael Mendonça França*

*   Remove deprecated `Benchmark.ms` method. It is now defined in the `benchmark` gem.

    *Rafael Mendonça França*

*   Remove deprecated addition for `Time` instances with `ActiveSupport::TimeWithZone`.

    *Rafael Mendonça França*

*   Remove deprecated support for `to_time` to preserve the system local time. It will now always preserve the receiver
    timezone.

    *Rafael Mendonça França*

*   Deprecate `config.active_support.to_time_preserves_timezone`.

    *Rafael Mendonça França*

*   Standardize event name formatting in `assert_event_reported` error messages.

    The event name in failure messages now uses `.inspect` (e.g., `name: "user.created"`)
    to match `assert_events_reported` and provide type clarity between strings and symbols.
    This only affects tests that assert on the failure message format itself.

    *George Ma*

*   Fix `Enumerable#sole` to return the full tuple instead of just the first element of the tuple.

    *Olivier Bellone*

*   Fix parallel tests hanging when worker processes die abruptly.

    Previously, if a worker process was killed (e.g., OOM killed, `kill -9`) during parallel
    test execution, the test suite would hang forever waiting for the dead worker.

    *Joshua Young*

*   Add `config.active_support.escape_js_separators_in_json`.

    Introduce a new framework default to skip escaping LINE SEPARATOR (U+2028) and PARAGRAPH SEPARATOR (U+2029) in JSON.

    Historically these characters were not valid inside JavaScript literal strings but that changed in ECMAScript 2019.
    As such it's no longer a concern in modern browsers: https://caniuse.com/mdn-javascript_builtins_json_json_superset.

    *Étienne Barrié*, *Jean Boussier*

*   Fix `NameError` when `class_attribute` is defined on instance singleton classes.

    Previously, calling `class_attribute` on an instance's singleton class would raise
    a `NameError` when accessing the attribute through the instance.

    ```ruby
    object = MyClass.new
    object.singleton_class.class_attribute :foo, default: "bar"
    object.foo # previously raised NameError, now returns "bar"
    ```

    *Joshua Young*

*   Introduce `ActiveSupport::Testing::EventReporterAssertions#with_debug_event_reporting`
    to enable event reporter debug mode in tests.

    The previous way to enable debug mode is by using `#with_debug` on the
    event reporter itself, which is too verbose. This new helper will help
    clear up any confusion on how to test debug events.

    *Gannon McGibbon*

*   Add `ActiveSupport::StructuredEventSubscriber` for consuming notifications and
    emitting structured event logs. Events may be emitted with the `#emit_event`
    or `#emit_debug_event` methods.

    ```ruby
    class MyStructuredEventSubscriber < ActiveSupport::StructuredEventSubscriber
      def notification(event)
        emit_event("my.notification", data: 1)
      end
    end
    ```

    *Adrianna Chang*

*   `ActiveSupport::FileUpdateChecker` does not depend on `Time.now` to prevent unecessary reloads with time travel test helpers

    *Jan Grodowski*

*   Add `ActiveSupport::Cache::Store#namespace=` and `#namespace`.

    Can be used as an alternative to `Store#clear` in some situations such as parallel
    testing.

    *Nick Schwaderer*

*   Create `parallel_worker_id` helper for running parallel tests. This allows users to
    know which worker they are currently running in.

    *Nick Schwaderer*

*   Make the cache of `ActiveSupport::Cache::Strategy::LocalCache::Middleware` updatable.

    If the cache client at `Rails.cache` of a booted application changes, the corresponding
    mounted middleware needs to update in order for request-local caches to be setup properly.
    Otherwise, redundant cache operations will erroneously hit the datastore.

    *Gannon McGibbon*

*   Add `assert_events_reported` test helper for `ActiveSupport::EventReporter`.

    This new assertion allows testing multiple events in a single block, regardless of order:

    ```ruby
    assert_events_reported([
      { name: "user.created", payload: { id: 123 } },
      { name: "email.sent", payload: { to: "user@example.com" } }
    ]) do
      create_user_and_send_welcome_email
    end
    ```

    *George Ma*

*   Add `ActiveSupport::TimeZone#standard_name` method.

    ``` ruby
    zone = ActiveSupport::TimeZone['Hawaii']
    # Old way
    ActiveSupport::TimeZone::MAPPING[zone.name]
    # New way
    zone.standard_name # => 'Pacific/Honolulu'
    ```

    *Bogdan Gusiev*

*   Add Structured Event Reporter, accessible via `Rails.event`.

    The Event Reporter provides a unified interface for producing structured events in Rails
    applications:

    ```ruby
    Rails.event.notify("user.signup", user_id: 123, email: "user@example.com")
    ```

    It supports adding tags to events:

    ```ruby
    Rails.event.tagged("graphql") do
      # Event includes tags: { graphql: true }
      Rails.event.notify("user.signup", user_id: 123, email: "user@example.com")
    end
    ```

    As well as context:
    ```ruby
    # All events will contain context: {request_id: "abc123", shop_id: 456}
    Rails.event.set_context(request_id: "abc123", shop_id: 456)
    ```

    Events are emitted to subscribers. Applications register subscribers to
    control how events are serialized and emitted. Subscribers must implement
    an `#emit` method, which receives the event hash:

    ```ruby
    class LogSubscriber
      def emit(event)
        payload = event[:payload].map { |key, value| "#{key}=#{value}" }.join(" ")
        source_location = event[:source_location]
        log = "[#{event[:name]}] #{payload} at #{source_location[:filepath]}:#{source_location[:lineno]}"
        Rails.logger.info(log)
      end
    end
    ```

    *Adrianna Chang*

*   Make `ActiveSupport::Logger` `#freeze`-friendly.

    *Joshua Young*

*   Make `ActiveSupport::Gzip.compress` deterministic based on input.

    `ActiveSupport::Gzip.compress` used to include a timestamp in the output,
    causing consecutive calls with the same input data to have different output
    if called during different seconds. It now always sets the timestamp to `0`
    so that the output is identical for any given input.

    *Rob Brackett*

*   Given an array of `Thread::Backtrace::Location` objects, the new method
    `ActiveSupport::BacktraceCleaner#clean_locations` returns an array with the
    clean ones:

    ```ruby
    clean_locations = backtrace_cleaner.clean_locations(caller_locations)
    ```

    Filters and silencers receive strings as usual. However, the `path`
    attributes of the locations in the returned array are the original,
    unfiltered ones, since locations are immutable.

    *Xavier Noria*

*   Improve `CurrentAttributes` and `ExecutionContext` state managment in test cases.

    Previously these two global state would be entirely cleared out whenever calling
    into code that is wrapped by the Rails executor, typically Action Controller or
    Active Job helpers:

    ```ruby
    test "#index works" do
      CurrentUser.id = 42
      get :index
      CurrentUser.id == nil
    end
    ```

    Now re-entering the executor properly save and restore that state.

    *Jean Boussier*

*   The new method `ActiveSupport::BacktraceCleaner#first_clean_location`
    returns the first clean location of the caller's call stack, or `nil`.
    Locations are `Thread::Backtrace::Location` objects. Useful when you want to
    report the application-level location where something happened as an object.

    *Xavier Noria*

*   FileUpdateChecker and EventedFileUpdateChecker ignore changes in Gem.path now.

    *Ermolaev Andrey*, *zzak*

*   The new method `ActiveSupport::BacktraceCleaner#first_clean_frame` returns
    the first clean frame of the caller's backtrace, or `nil`. Useful when you
    want to report the application-level frame where something happened as a
    string.

    *Xavier Noria*

*   Always clear `CurrentAttributes` instances.

    Previously `CurrentAttributes` instance would be reset at the end of requests.
    Meaning its attributes would be re-initialized.

    This is problematic because it assume these objects don't hold any state
    other than their declared attribute, which isn't always the case, and
    can lead to state leak across request.

    Now `CurrentAttributes` instances are abandoned at the end of a request,
    and a new instance is created at the start of the next request.

    *Jean Boussier*, *Janko Marohnić*

*   Add public API for `before_fork_hook` in parallel testing.

    Introduces a public API for calling the before fork hooks implemented by parallel testing.

    ```ruby
    parallelize_before_fork do
        # perform an action before test processes are forked
    end
    ```

    *Eileen M. Uchitelle*

*   Implement ability to skip creating parallel testing databases.

    With parallel testing, Rails will create a database per process. If this isn't
    desirable or you would like to implement databases handling on your own, you can
    now turn off this default behavior.

    To skip creating a database per process, you can change it via the
    `parallelize` method:

    ```ruby
    parallelize(workers: 10, parallelize_databases: false)
    ```

    or via the application configuration:

    ```ruby
    config.active_support.parallelize_databases = false
    ```

    *Eileen M. Uchitelle*

*   Allow to configure maximum cache key sizes

    When the key exceeds the configured limit (250 bytes by default), it will be truncated and
    the digest of the rest of the key appended to it.

    Note that previously `ActiveSupport::Cache::RedisCacheStore` allowed up to 1kb cache keys before
    truncation, which is now reduced to 250 bytes.

    ```ruby
    config.cache_store = :redis_cache_store, { max_key_size: 64 }
    ```

    *fatkodima*

*   Use `UNLINK` command instead of `DEL` in `ActiveSupport::Cache::RedisCacheStore` for non-blocking deletion.

    *Aron Roh*

*   Add `Cache#read_counter` and `Cache#write_counter`

    ```ruby
    Rails.cache.write_counter("foo", 1)
    Rails.cache.read_counter("foo") # => 1
    Rails.cache.increment("foo")
    Rails.cache.read_counter("foo") # => 2
    ```

    *Alex Ghiculescu*

*   Introduce ActiveSupport::Testing::ErrorReporterAssertions#capture_error_reports

    Captures all reported errors from within the block that match the given
    error class.

    ```ruby
    reports = capture_error_reports(IOError) do
      Rails.error.report(IOError.new("Oops"))
      Rails.error.report(IOError.new("Oh no"))
      Rails.error.report(StandardError.new)
    end

    assert_equal 2, reports.size
    assert_equal "Oops", reports.first.error.message
    assert_equal "Oh no", reports.last.error.message
    ```

    *Andrew Novoselac*

*   Introduce ActiveSupport::ErrorReporter#add_middleware

    When reporting an error, the error context middleware will be called with the reported error
    and base execution context. The stack may mutate the context hash. The mutated context will
    then be passed to error subscribers. Middleware receives the same parameters as `ErrorReporter#report`.

    *Andrew Novoselac*, *Sam Schmidt*

*   Change execution wrapping to report all exceptions, including `Exception`.

    If a more serious error like `SystemStackError` or `NoMemoryError` happens,
    the error reporter should be able to report these kinds of exceptions.

    *Gannon McGibbon*

*   `ActiveSupport::Testing::Parallelization.before_fork_hook` allows declaration of callbacks that
    are invoked immediately before forking test workers.

    *Mike Dalessio*

*   Allow the `#freeze_time` testing helper to accept a date or time argument.

    ```ruby
    Time.current # => Sun, 09 Jul 2024 15:34:49 EST -05:00
    freeze_time Time.current + 1.day
    sleep 1
    Time.current # => Mon, 10 Jul 2024 15:34:49 EST -05:00
    ```

    *Joshua Young*

*   `ActiveSupport::JSON` now accepts options

    It is now possible to pass options to `ActiveSupport::JSON`:
    ```ruby
    ActiveSupport::JSON.decode('{"key": "value"}', symbolize_names: true) # => { key: "value" }
    ```

    *matthaigh27*

*   `ActiveSupport::Testing::NotificationAssertions`'s `assert_notification` now matches against payload subsets by default.

    Previously the following assertion would fail due to excess key vals in the notification payload. Now with payload subset matching, it will pass.

    ```ruby
    assert_notification("post.submitted", title: "Cool Post") do
      ActiveSupport::Notifications.instrument("post.submitted", title: "Cool Post", body: "Cool Body")
    end
    ```

    Additionally, you can now persist a matched notification for more customized assertions.

    ```ruby
    notification = assert_notification("post.submitted", title: "Cool Post") do
      ActiveSupport::Notifications.instrument("post.submitted", title: "Cool Post", body: Body.new("Cool Body"))
    end

    assert_instance_of(Body, notification.payload[:body])
    ```

    *Nicholas La Roux*

*   Deprecate `String#mb_chars` and `ActiveSupport::Multibyte::Chars`.

    These APIs are a relic of the Ruby 1.8 days when Ruby strings weren't encoding
    aware. There is no legitimate reasons to need these APIs today.

    *Jean Boussier*

*   Deprecate `ActiveSupport::Configurable`

    *Sean Doyle*

*   `nil.to_query("key")` now returns `key`.

    Previously it would return `key=`, preventing round tripping with `Rack::Utils.parse_nested_query`.

    *Erol Fornoles*

*   Avoid wrapping redis in a `ConnectionPool` when using `ActiveSupport::Cache::RedisCacheStore` if the `:redis`
    option is already a `ConnectionPool`.

    *Joshua Young*

*   Alter `ERB::Util.tokenize` to return :PLAIN token with full input string when string doesn't contain ERB tags.

    *Martin Emde*

*   Fix a bug in `ERB::Util.tokenize` that causes incorrect tokenization when ERB tags are preceded by multibyte characters.

    *Martin Emde*

*   Add `ActiveSupport::Testing::NotificationAssertions` module to help with testing `ActiveSupport::Notifications`.

    *Nicholas La Roux*, *Yishu See*, *Sean Doyle*

*   `ActiveSupport::CurrentAttributes#attributes` now will return a new hash object on each call.

    Previously, the same hash object was returned each time that method was called.

    *fatkodima*

*   `ActiveSupport::JSON.encode` supports CIDR notation.

    Previously:

    ```ruby
    ActiveSupport::JSON.encode(IPAddr.new("172.16.0.0/24")) # => "\"172.16.0.0\""
    ```

    After this change:

    ```ruby
    ActiveSupport::JSON.encode(IPAddr.new("172.16.0.0/24")) # => "\"172.16.0.0/24\""
    ```

    *Taketo Takashima*

*   Make `ActiveSupport::FileUpdateChecker` faster when checking many file-extensions.

    *Jonathan del Strother*

## Active Model

*   Add `reset_token: { expires_in: ... }` option to `has_secure_password`.

    Allows configuring the expiry duration of password reset tokens (default remains 15 minutes for backwards compatibility).

    ```ruby
    has_secure_password reset_token: { expires_in: 1.hour }
    ```

    *Jevin Sew*, *Abeid Ahmed*

*   Add `except_on:` option for validation callbacks.

    *Ben Sheldon*

*   Backport `ActiveRecord::Normalization` to `ActiveModel::Attributes::Normalization`

    ```ruby
    class User
      include ActiveModel::Attributes
      include ActiveModel::Attributes::Normalization

      attribute :email, :string

      normalizes :email, with: -> email { email.strip.downcase }
    end

    user = User.new
    user.email =    " CRUISE-CONTROL@EXAMPLE.COM\n"
    user.email # => "cruise-control@example.com"
    ```

    *Sean Doyle*

## Active Record

*   Fix SQLite3 data loss during table alterations with CASCADE foreign keys.

    When altering a table in SQLite3 that is referenced by child tables with
    `ON DELETE CASCADE` foreign keys, ActiveRecord would silently delete all
    data from the child tables. This occurred because SQLite requires table
    recreation for schema changes, and during this process the original table
    is temporarily dropped, triggering CASCADE deletes on child tables.

    The root cause was incorrect ordering of operations. The original code
    wrapped `disable_referential_integrity` inside a transaction, but
    `PRAGMA foreign_keys` cannot be modified inside a transaction in SQLite -
    attempting to do so simply has no effect. This meant foreign keys remained
    enabled during table recreation, causing CASCADE deletes to fire.

    The fix reverses the order to follow the official SQLite 12-step ALTER TABLE
    procedure: `disable_referential_integrity` now wraps the transaction instead
    of being wrapped by it. This ensures foreign keys are properly disabled
    before the transaction starts and re-enabled after it commits, preventing
    CASCADE deletes while maintaining data integrity through atomic transactions.

    *Ruy Rocha*

*   Add replicas to test database parallelization setup.

    Setup and configuration of databases for parallel testing now includes replicas.

    This fixes an issue when using a replica database, database selector middleware,
    and non-transactional tests, where integration tests running in parallel would select
    the base test database, i.e. `db_test`, instead of the numbered parallel worker database,
    i.e. `db_test_{n}`.

    *Adam Maas*

*   Support virtual (not persisted) generated columns on PostgreSQL 18+

    PostgreSQL 18 introduces virtual (not persisted) generated columns,
    which are now the default unless the `stored: true` option is explicitly specified on PostgreSQL 18+.

    ```ruby
    create_table :users do |t|
      t.string :name
      t.virtual :lower_name,  type: :string,  as: "LOWER(name)", stored: false
      t.virtual :name_length, type: :integer, as: "LENGTH(name)"
    end
    ```

    *Yasuo Honda*

*   Optimize schema dumping to prevent duplicate file generation.

    `ActiveRecord::Tasks::DatabaseTasks.dump_all` now tracks which schema files
    have already been dumped and skips dumping the same file multiple times.
    This improves performance when multiple database configurations share the
    same schema dump path.

    *Mikey Gough*, *Hartley McGuire*

*   Add structured events for Active Record:
    - `active_record.strict_loading_violation`
    - `active_record.sql`

    *Gannon McGibbon*

*   Add support for integer shard keys.
    ```ruby
    # Now accepts symbols as shard keys.
    ActiveRecord::Base.connects_to(shards: {
      1: { writing: :primary_shard_one, reading: :primary_shard_one },
      2: { writing: :primary_shard_two, reading: :primary_shard_two},
    })

    ActiveRecord::Base.connected_to(shard: 1) do
      # ..
    end
    ```

    *Nony Dutton*

*   Add `ActiveRecord::Base.only_columns`

    Similar in use case to `ignored_columns` but listing columns to consider rather than the ones
    to ignore.

    Can be useful when working with a legacy or shared database schema, or to make safe schema change
    in two deploys rather than three.

    *Anton Kandratski*

*   Use `PG::Connection#close_prepared` (protocol level Close) to deallocate
    prepared statements when available.

    To enable its use, you must have pg >= 1.6.0, libpq >= 17, and a PostgreSQL
    database version >= 17.

    *Hartley McGuire*, *Andrew Jackson*

*   Fix query cache for pinned connections in multi threaded transactional tests

    When a pinned connection is used across separate threads, they now use a separate cache store
    for each thread.

    This improve accuracy of system tests, and any test using multiple threads.

    *Heinrich Lee Yu*, *Jean Boussier*

*   Fix time attribute dirty tracking with timezone conversions.

    Time-only attributes now maintain a fixed date of 2000-01-01 during timezone conversions,
    preventing them from being incorrectly marked as changed due to date shifts.

    This fixes an issue where time attributes would be marked as changed when setting the same time value
    due to timezone conversion causing internal date shifts.

    *Prateek Choudhary*

*   Skip calling `PG::Connection#cancel` in `cancel_any_running_query`
    when using libpq >= 18 with pg < 1.6.0, due to incompatibility.
    Rollback still runs, but may take longer.

    *Yasuo Honda*, *Lars Kanis*

*   Don't add `id_value` attribute alias when attribute/column with that name already exists.

    *Rob Lewis*

*   Remove deprecated `:unsigned_float` and `:unsigned_decimal` column methods for MySQL.

    *Rafael Mendonça França*

*   Remove deprecated `:retries` option for the SQLite3 adapter.

    *Rafael Mendonça França*

*   Introduce new database configuration options `keepalive`, `max_age`, and
    `min_connections` -- and rename `pool` to `max_connections` to match.

    There are no changes to default behavior, but these allow for more specific
    control over pool behavior.

    *Matthew Draper*, *Chris AtLee*, *Rachael Wright-Munn*

*   Move `LIMIT` validation from query generation to when `limit()` is called.

    *Hartley McGuire*, *Shuyang*

*   Add `ActiveRecord::CheckViolation` error class for check constraint violations.

    *Ryuta Kamizono*

*   Add `ActiveRecord::ExclusionViolation` error class for exclusion constraint violations.

    When an exclusion constraint is violated in PostgreSQL, the error will now be raised
    as `ActiveRecord::ExclusionViolation` instead of the generic `ActiveRecord::StatementInvalid`,
    making it easier to handle these specific constraint violations in application code.

    This follows the same pattern as other constraint violation error classes like
    `RecordNotUnique` for unique constraint violations and `InvalidForeignKey` for
    foreign key constraint violations.

    *Ryuta Kamizono*

*   Attributes filtered by `filter_attributes` will now also be filtered by `filter_parameters`
    so sensitive information is not leaked.

    *Jill Klang*

*   Add `connection.current_transaction.isolation` API to check current transaction's isolation level.

    Returns the isolation level if it was explicitly set via the `isolation:` parameter
    or through `ActiveRecord.with_transaction_isolation_level`, otherwise returns `nil`.
    Nested transactions return the parent transaction's isolation level.

    ```ruby
    # Returns nil when no transaction
    User.connection.current_transaction.isolation # => nil

    # Returns explicitly set isolation level
    User.transaction(isolation: :serializable) do
      User.connection.current_transaction.isolation # => :serializable
    end

    # Returns nil when isolation not explicitly set
    User.transaction do
      User.connection.current_transaction.isolation # => nil
    end

    # Nested transactions inherit parent's isolation
    User.transaction(isolation: :read_committed) do
      User.transaction do
        User.connection.current_transaction.isolation # => :read_committed
      end
    end
    ```

    *Kir Shatrov*

*   Fix `#merge` with `#or` or `#and` and a mixture of attributes and SQL strings resulting in an incorrect query.

    ```ruby
    base = Comment.joins(:post).where(user_id: 1).where("recent = 1")
    puts base.merge(base.where(draft: true).or(Post.where(archived: true))).to_sql
    ```

    Before:

    ```SQL
    SELECT "comments".* FROM "comments"
    INNER JOIN "posts" ON "posts"."id" = "comments"."post_id"
    WHERE (recent = 1)
    AND (
      "comments"."user_id" = 1
      AND (recent = 1)
      AND "comments"."draft" = 1
      OR "posts"."archived" = 1
    )
    ```

    After:

    ```SQL
    SELECT "comments".* FROM "comments"
    INNER JOIN "posts" ON "posts"."id" = "comments"."post_id"
    WHERE "comments"."user_id" = 1
    AND (recent = 1)
    AND (
      "comments"."user_id" = 1
      AND (recent = 1)
      AND "comments"."draft" = 1
      OR "posts"."archived" = 1
    )
    ```

    *Joshua Young*

*   Make schema dumper to account for `ActiveRecord.dump_schemas` when dumping in `:ruby` format.

    *fatkodima*

*   Add `:touch` option to `update_column`/`update_columns` methods.

    ```ruby
    # Will update :updated_at/:updated_on alongside :nice column.
    user.update_column(:nice, true, touch: true)

    # Will update :updated_at/:updated_on alongside :last_ip column
    user.update_columns(last_ip: request.remote_ip, touch: true)
    ```

    *Dmitrii Ivliev*

*   Optimize Active Record batching further when using ranges.

    Tested on a PostgreSQL table with 10M records and batches of 10k records, the generation
    of relations for the 1000 batches was `4.8x` faster (`6.8s` vs. `1.4s`), used `900x`
    less bandwidth (`180MB` vs. `0.2MB`) and allocated `45x` less memory (`490MB` vs. `11MB`).

    *Maxime Réty*, *fatkodima*

*   Include current character length in error messages for index and table name length validations.

    *Joshua Young*

*   Add `rename_schema` method for PostgreSQL.

    *T S Vallender*

*   Implement support for deprecating associations:

    ```ruby
    has_many :posts, deprecated: true
    ```

    With that, Active Record will report any usage of the `posts` association.

    Three reporting modes are supported (`:warn`, `:raise`, and `:notify`), and
    backtraces can be enabled or disabled. Defaults are `:warn` mode and
    disabled backtraces.

    Please, check the docs for further details.

    *Xavier Noria*

*   PostgreSQL adapter create DB now supports `locale_provider` and `locale`.

    *Bengt-Ove Hollaender*

*   Use ntuples to populate row_count instead of count for Postgres

    *Jonathan Calvert*

*   Fix checking whether an unpersisted record is `include?`d in a strictly
    loaded `has_and_belongs_to_many` association.

    *Hartley McGuire*

*   Add ability to change transaction isolation for all pools within a block.

    This functionality is useful if your application needs to change the database
    transaction isolation for a request or action.

    Calling `ActiveRecord.with_transaction_isolation_level(level) {}` in an around filter or
    middleware will set the transaction isolation for all pools accessed within the block,
    but not for the pools that aren't.

    This works with explicit and implicit transactions:

    ```ruby
    ActiveRecord.with_transaction_isolation_level(:read_committed) do
      Tag.transaction do # opens a transaction explicitly
        Tag.create!
      end
    end
    ```

    ```ruby
    ActiveRecord.with_transaction_isolation_level(:read_committed) do
      Tag.create! # opens a transaction implicitly
    end
    ```

    *Eileen M. Uchitelle*

*   Raise `ActiveRecord::MissingRequiredOrderError` when order dependent finder methods (e.g. `#first`, `#last`) are
    called without `order` values on the relation, and the model does not have any order columns (`implicit_order_column`,
    `query_constraints`, or `primary_key`) to fall back on.

    This change will be introduced with a new framework default for Rails 8.1, and the current behavior of not raising
    an error has been deprecated with the aim of removing the configuration option in Rails 8.2.

    ```ruby
    config.active_record.raise_on_missing_required_finder_order_columns = true
    ```

    *Joshua Young*

*   `:class_name` is now invalid in polymorphic `belongs_to` associations.

    Reason is `:class_name` does not make sense in those associations because
    the class name of target records is dynamic and stored in the type column.

    Existing polymorphic associations setting this option can just delete it.
    While it did not raise, it had no effect anyway.

    *Xavier Noria*

*   Add support for multiple databases to `db:migrate:reset`.

    *Joé Dupuis*

*   Add `affected_rows` to `ActiveRecord::Result`.

    *Jenny Shen*

*   Enable passing retryable SqlLiterals to `#where`.

    *Hartley McGuire*

*   Set default for primary keys in `insert_all`/`upsert_all`.

    Previously in Postgres, updating and inserting new records in one upsert wasn't possible
    due to null primary key values. `nil` primary key values passed into `insert_all`/`upsert_all`
    are now implicitly set to the default insert value specified by adapter.

    *Jenny Shen*

*   Add a load hook `active_record_database_configurations` for `ActiveRecord::DatabaseConfigurations`

    *Mike Dalessio*

*   Use `TRUE` and `FALSE` for SQLite queries with boolean columns.

    *Hartley McGuire*

*   Bump minimum supported SQLite to 3.23.0.

    *Hartley McGuire*

*   Allow allocated Active Records to lookup associations.

    Previously, the association cache isn't setup on allocated record objects, so association
    lookups will crash. Test frameworks like mocha use allocate to check for stubbable instance
    methods, which can trigger an association lookup.

    *Gannon McGibbon*

*   Encryption now supports `support_unencrypted_data: true` being set per-attribute.

    Previously this only worked if `ActiveRecord::Encryption.config.support_unencrypted_data == true`.
    Now, if the global config is turned off, you can still opt in for a specific attribute.

    ```ruby
    # ActiveRecord::Encryption.config.support_unencrypted_data = true
    class User < ActiveRecord::Base
      encrypts :name, support_unencrypted_data: false # only supports encrypted data
      encrypts :email # supports encrypted or unencrypted data
    end
    ```

    ```ruby
    # ActiveRecord::Encryption.config.support_unencrypted_data = false
    class User < ActiveRecord::Base
      encrypts :name, support_unencrypted_data: true # supports encrypted or unencrypted data
      encrypts :email  # only supports encrypted data
    end
    ```

    *Alex Ghiculescu*

*   Model generator no longer needs a database connection to validate column types.

    *Mike Dalessio*

*   Allow signed ID verifiers to be configurable via `Rails.application.message_verifiers`

    Prior to this change, the primary way to configure signed ID verifiers was
    to set `signed_id_verifier` on each model class:

      ```ruby
      Post.signed_id_verifier = ActiveSupport::MessageVerifier.new(...)
      Comment.signed_id_verifier = ActiveSupport::MessageVerifier.new(...)
      ```

    And if the developer did not set `signed_id_verifier`, a verifier would be
    instantiated with a secret derived from `secret_key_base` and the following
    options:

      ```ruby
      { digest: "SHA256", serializer: JSON, url_safe: true }
      ```

    Thus it was cumbersome to rotate configuration for all verifiers.

    This change defines a new Rails config: [`config.active_record.use_legacy_signed_id_verifier`][].
    The default value is `:generate_and_verify`, which preserves the previous
    behavior. However, when set to `:verify`, signed ID verifiers will use
    configuration from `Rails.application.message_verifiers` (specifically,
    `Rails.application.message_verifiers["active_record/signed_id"]`) to
    generate and verify signed IDs, but will also verify signed IDs using the
    older configuration.

    To avoid complication, the new behavior only applies when `signed_id_verifier_secret`
    is not set on a model class or any of its ancestors. Additionally,
    `signed_id_verifier_secret` is now deprecated. If you are currently setting
    `signed_id_verifier_secret` on a model class, you can set `signed_id_verifier`
    instead:

      ```ruby
      # BEFORE
      Post.signed_id_verifier_secret = "my secret"

      # AFTER
      Post.signed_id_verifier = ActiveSupport::MessageVerifier.new("my secret", digest: "SHA256", serializer: JSON, url_safe: true)
      ```

    To ease migration, `signed_id_verifier` has also been changed to behave as a
    `class_attribute` (i.e. inheritable), but _only when `signed_id_verifier_secret`
    is not set_:

      ```ruby
      # BEFORE
      ActiveRecord::Base.signed_id_verifier = ActiveSupport::MessageVerifier.new(...)
      Post.signed_id_verifier == ActiveRecord::Base.signed_id_verifier # => false

      # AFTER
      ActiveRecord::Base.signed_id_verifier = ActiveSupport::MessageVerifier.new(...)
      Post.signed_id_verifier == ActiveRecord::Base.signed_id_verifier # => true

      Post.signed_id_verifier_secret = "my secret" # => deprecation warning
      Post.signed_id_verifier == ActiveRecord::Base.signed_id_verifier # => false
      ```

    Note, however, that it is recommended to eventually migrate from
    model-specific verifiers to a unified configuration managed by
    `Rails.application.message_verifiers`. `ActiveSupport::MessageVerifier#rotate`
    can facilitate that transition. For example:

      ```ruby
      # BEFORE
      # Generate and verify signed Post IDs using Post-specific configuration
      Post.signed_id_verifier = ActiveSupport::MessageVerifier.new("post secret", ...)

      # AFTER
      # Generate and verify signed Post IDs using the unified configuration
      Post.signed_id_verifier = Post.signed_id_verifier.dup
      # Fall back to Post-specific configuration when verifying signed IDs
      Post.signed_id_verifier.rotate("post secret", ...)
      ```

    [`config.active_record.use_legacy_signed_id_verifier`]: https://guides.rubyonrails.org/v8.1/configuring.html#config-active-record-use-legacy-signed-id-verifier

    *Ali Sepehri*, *Jonathan Hefner*

*   Prepend `extra_flags` in postgres' `structure_load`

    When specifying `structure_load_flags` with a postgres adapter, the flags
    were appended to the default flags, instead of prepended.
    This caused issues with flags not being taken into account by postgres.

    *Alice Loeser*

*   Allow bypassing primary key/constraint addition in `implicit_order_column`

    When specifying multiple columns in an array for `implicit_order_column`, adding
    `nil` as the last element will prevent appending the primary key to order
    conditions. This allows more precise control of indexes used by
    generated queries. It should be noted that this feature does introduce the risk
    of API misbehavior if the specified columns are not fully unique.

    *Issy Long*

*   Allow setting the `schema_format` via database configuration.

    ```
    primary:
      schema_format: ruby
    ```

    Useful for multi-database setups when apps require different formats per-database.

    *T S Vallender*

*   Support disabling indexes for MySQL v8.0.0+ and MariaDB v10.6.0+

    MySQL 8.0.0 added an option to disable indexes from being used by the query
    optimizer by making them "invisible". This allows the index to still be maintained
    and updated but no queries will be permitted to use it. This can be useful for adding
    new invisible indexes or making existing indexes invisible before dropping them
    to ensure queries are not negatively affected.
    See https://dev.mysql.com/blog-archive/mysql-8-0-invisible-indexes/ for more details.

    MariaDB 10.6.0 also added support for this feature by allowing indexes to be "ignored"
    in queries. See https://mariadb.com/kb/en/ignored-indexes/ for more details.

    Active Record now supports this option for MySQL 8.0.0+ and MariaDB 10.6.0+ for
    index creation and alteration where the new index option `enabled: true/false` can be
    passed to column and index methods as below:

    ```ruby
    add_index :users, :email, enabled: false
    enable_index :users, :email
    add_column :users, :dob, :string, index: { enabled: false }

    change_table :users do |t|
      t.index :name, enabled: false
      t.index :dob
      t.disable_index :dob
      t.column :username, :string, index: { enabled: false }
      t.references :account, index: { enabled: false }
    end

    create_table :users do |t|
      t.string :name, index: { enabled: false }
      t.string :email
      t.index :email, enabled: false
    end
    ```

    *Merve Taner*

*   Respect `implicit_order_column` in `ActiveRecord::Relation#reverse_order`.

    *Joshua Young*

*   Add column types to `ActiveRecord::Result` for SQLite3.

    *Andrew Kane*

*   Raise `ActiveRecord::ReadOnlyError` when pessimistically locking with a readonly role.

    *Joshua Young*

*   Fix using the `SQLite3Adapter`'s `dbconsole` method outside of a Rails application.

    *Hartley McGuire*

*   Fix migrating multiple databases with `ActiveRecord::PendingMigration` action.

    *Gannon McGibbon*

*   Enable automatically retrying idempotent association queries on connection
    errors.

    *Hartley McGuire*

*   Add `allow_retry` to `sql.active_record` instrumentation.

    This enables identifying queries which queries are automatically retryable on connection errors.

    *Hartley McGuire*

*   Better support UPDATE with JOIN for Postgresql and SQLite3

    Previously when generating update queries with one or more JOIN clauses,
    Active Record would use a sub query which would prevent to reference the joined
    tables in the `SET` clause, for instance:

    ```ruby
    Comment.joins(:post).update_all("title = posts.title")
    ```

    This is now supported as long as the relation doesn't also use a `LIMIT`, `ORDER` or
    `GROUP BY` clause. This was supported by the MySQL adapter for a long time.

    *Jean Boussier*

*   Introduce a before-fork hook in `ActiveSupport::Testing::Parallelization` to clear existing
    connections, to avoid fork-safety issues with the mysql2 adapter.

    Fixes #41776

    *Mike Dalessio*, *Donal McBreen*

*   PoolConfig no longer keeps a reference to the connection class.

    Keeping a reference to the class caused subtle issues when combined with reloading in
    development. Fixes #54343.

    *Mike Dalessio*

*   Fix SQL notifications sometimes not sent when using async queries.

    ```ruby
    Post.async_count
    ActiveSupport::Notifications.subscribed(->(*) { "Will never reach here" }) do
      Post.count
    end
    ```

    In rare circumstances and under the right race condition, Active Support notifications
    would no longer be dispatched after using an asynchronous query.
    This is now fixed.

    *Edouard Chin*

*   Eliminate queries loading dumped schema cache on Postgres

    Improve resiliency by avoiding needing to open a database connection to load the
    type map while defining attribute methods at boot when a schema cache file is
    configured on PostgreSQL databases.

    *James Coleman*

*   `ActiveRecord::Coder::JSON` can be instantiated

    Options can now be passed to `ActiveRecord::Coder::JSON` when instantiating the coder. This allows:
    ```ruby
    serialize :config, coder: ActiveRecord::Coder::JSON.new(symbolize_names: true)
    ```
    *matthaigh27*

*   Deprecate using `insert_all`/`upsert_all` with unpersisted records in associations.

    Using these methods on associations containing unpersisted records will now
    show a deprecation warning, as the unpersisted records will be lost after
    the operation.

    *Nick Schwaderer*

*   Make column name optional for `index_exists?`.

    This aligns well with `remove_index` signature as well, where
    index name doesn't need to be derived from the column names.

    *Ali Ismayiliov*

*   Change the payload name of `sql.active_record` notification for eager
    loading from "SQL" to "#{model.name} Eager Load".

    *zzak*

*   Enable automatically retrying idempotent `#exists?` queries on connection
    errors.

    *Hartley McGuire*, *classidied*

*   Deprecate usage of unsupported methods in conjunction with `update_all`:

    `update_all` will now print a deprecation message if a query includes either `WITH`,
    `WITH RECURSIVE` or `DISTINCT` statements. Those were never supported and were ignored
    when generating the SQL query.

    An error will be raised in a future Rails release. This behavior will be consistent
    with `delete_all` which currently raises an error for unsupported statements.

    *Edouard Chin*

*   The table columns inside `schema.rb` are now sorted alphabetically.

    Previously they'd be sorted by creation order, which can cause merge conflicts when two
    branches modify the same table concurrently.

    *John Duff*

*   Introduce versions formatter for the schema dumper.

    It is now possible to override how schema dumper formats versions information inside the
    `structure.sql` file. Currently, the versions are simply sorted in the decreasing order.
    Within large teams, this can potentially cause many merge conflicts near the top of the list.

    Now, the custom formatter can be provided with a custom sorting logic (e.g. by hash values
    of the versions), which can greatly reduce the number of conflicts.

    *fatkodima*

*   Serialized attributes can now be marked as comparable.

    A not rare issue when working with serialized attributes is that the serialized representation of an object
    can change over time. Either because you are migrating from one serializer to the other (e.g. YAML to JSON or to msgpack),
    or because the serializer used subtly changed its output.

    One example is libyaml that used to have some extra trailing whitespaces, and recently fixed that.
    When this sorts of thing happen, you end up with lots of records that report being changed even though
    they aren't, which in the best case leads to a lot more writes to the database and in the worst case lead to nasty bugs.

    The solution is to instead compare the deserialized representation of the object, however Active Record
    can't assume the deserialized object has a working `==` method. Hence why this new functionality is opt-in.

    ```ruby
    serialize :config, type: Hash, coder: JSON, comparable: true
    ```

    *Jean Boussier*

*   Fix MySQL default functions getting dropped when changing a column's nullability.

    *Bastian Bartmann*

*   SQLite extensions can be configured in `config/database.yml`.

    The database configuration option `extensions:` allows an application to load SQLite extensions
    when using `sqlite3` >= v2.4.0. The array members may be filesystem paths or the names of
    modules that respond to `.to_path`:

    ``` yaml
    development:
      adapter: sqlite3
      extensions:
        - SQLean::UUID                     # module name responding to `.to_path`
        - .sqlpkg/nalgeon/crypto/crypto.so # or a filesystem path
        - <%= AppExtensions.location %>    # or ruby code returning a path
    ```

    *Mike Dalessio*

*   `ActiveRecord::Middleware::ShardSelector` supports granular database connection switching.

    A new configuration option, `class_name:`, is introduced to
    `config.active_record.shard_selector` to allow an application to specify the abstract connection
    class to be switched by the shard selection middleware. The default class is
    `ActiveRecord::Base`.

    For example, this configuration tells `ShardSelector` to switch shards using
    `AnimalsRecord.connected_to`:

    ```
    config.active_record.shard_selector = { class_name: "AnimalsRecord" }
    ```

    *Mike Dalessio*

*   Reset relations after `insert_all`/`upsert_all`.

    Bulk insert/upsert methods will now call `reset` if used on a relation, matching the behavior of `update_all`.

    *Milo Winningham*

*   Use `_N` as a parallel tests databases suffixes

    Peviously, `-N` was used as a suffix. This can cause problems for RDBMSes
    which do not support dashes in database names.

    *fatkodima*

*   Remember when a database connection has recently been verified (for
    two seconds, by default), to avoid repeated reverifications during a
    single request.

    This should recreate a similar rate of verification as in Rails 7.1,
    where connections are leased for the duration of a request, and thus
    only verified once.

    *Matthew Draper*

*   Allow to reset cache counters for multiple records.

    ```
    Aircraft.reset_counters([1, 2, 3], :wheels_count)
    ```

    It produces much fewer queries compared to the custom implementation using looping over ids.
    Previously: `O(ids.size * counters.size)` queries, now: `O(ids.size + counters.size)` queries.

    *fatkodima*

*   Add `affected_rows` to `sql.active_record` Notification.

    *Hartley McGuire*

*   Fix `sum` when performing a grouped calculation.

    `User.group(:friendly).sum` no longer worked. This is fixed.

    *Edouard Chin*

*   Add support for enabling or disabling transactional tests per database.

    A test class can now override the default `use_transactional_tests` setting
    for individual databases, which can be useful if some databases need their
    current state to be accessible to an external process while tests are running.

    ```ruby
    class MostlyTransactionalTest < ActiveSupport::TestCase
      self.use_transactional_tests = true
      skip_transactional_tests_for_database :shared
    end
    ```

    *Matthew Cheetham*, *Morgan Mareve*

*   Cast `query_cache` value when using URL configuration.

    *zzak*

*   NULLS NOT DISTINCT works with UNIQUE CONSTRAINT as well as UNIQUE INDEX.

    *Ryuta Kamizono*

*   `PG::UnableToSend: no connection to the server` is now retryable as a connection-related exception

    *Kazuma Watanabe*

## Action View

*   The BEGIN template annotation/comment was previously printed on the same line as the following element. We now insert a newline inside the comment so it spans two lines without adding visible whitespace to the HTML output to enhance readability.

    Before:
    ```
    <!-- BEGIN /Users/siaw23/Desktop/rails/actionview/test/fixtures/actionpack/test/greeting.html.erb --><p>This is grand!</p>
    ```

    After:
    ```
    <!-- BEGIN /Users/siaw23/Desktop/rails/actionview/test/fixtures/actionpack/test/greeting.html.erb
    --><p>This is grand!</p>
    ```
    *Emmanuel Hayford*

*   Add structured events for Action View:
    - `action_view.render_template`
    - `action_view.render_partial`
    - `action_view.render_layout`
    - `action_view.render_collection`
    - `action_view.render_start`

    *Gannon McGibbon*

*   Fix label with `for` option not getting prefixed by form `namespace` value

    *Abeid Ahmed*, *Hartley McGuire*

*   Add `fetchpriority` to Link headers to match HTML generated by `preload_link_tag`.

    *Guillermo Iguaran*

*   Add CSP `nonce` to Link headers generated by `preload_link_tag`.

    *Alexander Gitter*

*   Allow `current_page?` to match against specific HTTP method(s) with a `method:` option.

    *Ben Sheldon*

*   Remove `autocomplete="off"` on hidden inputs generated by the following
    tags:

    * `form_tag`, `token_tag`, `method_tag`

    As well as the hidden parameter fields included in `button_to`,
    `check_box`, `select` (with `multiple`) and `file_field` forms.

    *nkulway*

*   Enable configuring the strategy for tracking dependencies between Action
    View templates.

    The existing `:regex` strategy is kept as the default, but with
    `load_defaults 8.1` the strategy will be `:ruby` (using a real Ruby parser).

    *Hartley McGuire*

*   Introduce `relative_time_in_words` helper

    ```ruby
    relative_time_in_words(3.minutes.from_now) # => "in 3 minutes"
    relative_time_in_words(3.minutes.ago) # => "3 minutes ago"
    relative_time_in_words(10.seconds.ago, include_seconds: true) # => "less than 10 seconds ago"
    ```

    *Matheus Richard*

*   Make `nonce: false` remove the nonce attribute from `javascript_tag`, `javascript_include_tag`, and `stylesheet_link_tag`.

    *francktrouillez*

*   Add `dom_target` helper to create `dom_id`-like strings from an unlimited
    number of objects.

    *Ben Sheldon*

*   Respect `html_options[:form]` when `collection_checkboxes` generates the
    hidden `<input>`.

    *Riccardo Odone*

*   Layouts have access to local variables passed to `render`.

    This fixes #31680 which was a regression in Rails 5.1.

    *Mike Dalessio*

*   Argument errors related to strict locals in templates now raise an
    `ActionView::StrictLocalsError`, and all other argument errors are reraised as-is.

    Previously, any `ArgumentError` raised during template rendering was swallowed during strict
    local error handling, so that an `ArgumentError` unrelated to strict locals (e.g., a helper
    method invoked with incorrect arguments) would be replaced by a similar `ArgumentError` with an
    unrelated backtrace, making it difficult to debug templates.

    Now, any `ArgumentError` unrelated to strict locals is reraised, preserving the original
    backtrace for developers.

    Also note that `ActionView::StrictLocalsError` is a subclass of `ArgumentError`, so any existing
    code that rescues `ArgumentError` will continue to work.

    Fixes #52227.

    *Mike Dalessio*

*   Improve error highlighting of multi-line methods in ERB templates or
    templates where the error occurs within a do-end block.

    *Martin Emde*

*   Fix a crash in ERB template error highlighting when the error occurs on a
    line in the compiled template that is past the end of the source template.

    *Martin Emde*

*   Improve reliability of ERB template error highlighting.
    Fix infinite loops and crashes in highlighting and
    improve tolerance for alternate ERB handlers.

    *Martin Emde*

*   Allow `hidden_field` and `hidden_field_tag` to accept a custom autocomplete value.

    *brendon*

*   Add a new configuration `content_security_policy_nonce_auto` for automatically adding a nonce to the tags affected by the directives specified by the `content_security_policy_nonce_directives` configuration option.

    *francktrouillez*

## Action Pack

*   Submit test requests using `as: :html` with `Content-Type: x-www-form-urlencoded`

    *Sean Doyle*

*   Add link-local IP ranges to `ActionDispatch::RemoteIp` default proxies.

    Link-local addresses (`169.254.0.0/16` for IPv4 and `fe80::/10` for IPv6)
    are now included in the default trusted proxy list, similar to private IP ranges.

    *Adam Daniels*

*   `remote_ip` will no longer ignore IPs in X-Forwarded-For headers if they
    are accompanied by port information.

    *Duncan Brown*, *Prevenios Marinos*, *Masafumi Koba*, *Adam Daniels*

*   Add `action_dispatch.verbose_redirect_logs` setting that logs where redirects were called from.

    Similar to `active_record.verbose_query_logs` and `active_job.verbose_enqueue_logs`, this adds a line in your logs that shows where a redirect was called from.

    Example:

    ```
    Redirected to http://localhost:3000/posts/1
    ↳ app/controllers/posts_controller.rb:32:in `block (2 levels) in create'
    ```

    *Dennis Paagman*

*   Add engine route filtering and better formatting in `bin/rails routes`.

    Allow engine routes to be filterable in the routing inspector, and
    improve formatting of engine routing output.

    Before:
    ```
    > bin/rails routes -e engine_only
    No routes were found for this grep pattern.
    For more information about routes, see the Rails guide: https://guides.rubyonrails.org/routing.html.
    ```

    After:
    ```
    > bin/rails routes -e engine_only
    Routes for application:
    No routes were found for this grep pattern.
    For more information about routes, see the Rails guide: https://guides.rubyonrails.org/routing.html.

    Routes for Test::Engine:
    Prefix Verb URI Pattern       Controller#Action
    engine GET  /engine_only(.:format) a#b
    ```

    *Dennis Paagman*, *Gannon McGibbon*

*   Add structured events for Action Pack and Action Dispatch:
    - `action_dispatch.redirect`
    - `action_controller.request_started`
    - `action_controller.request_completed`
    - `action_controller.callback_halted`
    - `action_controller.rescue_from_handled`
    - `action_controller.file_sent`
    - `action_controller.redirected`
    - `action_controller.data_sent`
    - `action_controller.unpermitted_parameters`
    - `action_controller.fragment_cache`

    *Adrianna Chang*

*   URL helpers for engines mounted at the application root handle `SCRIPT_NAME` correctly.

    Fixed an issue where `SCRIPT_NAME` is not applied to paths generated for routes in an engine
    mounted at "/".

    *Mike Dalessio*

*   Update `ActionController::Metal::RateLimiting` to support passing method names to `:by` and `:with`

    ```ruby
    class SignupsController < ApplicationController
      rate_limit to: 10, within: 1.minute, with: :redirect_with_flash

      private
        def redirect_with_flash
          redirect_to root_url, alert: "Too many requests!"
        end
    end
    ```

    *Sean Doyle*

*   Optimize `ActionDispatch::Http::URL.build_host_url` when protocol is included in host.

    When using URL helpers with a host that includes the protocol (e.g., `{ host: "https://example.com" }`),
    skip unnecessary protocol normalization and string duplication since the extracted protocol is already
    in the correct format. This eliminates 2 string allocations per URL generation and provides a ~10%
    performance improvement for this case.

    *Joshua Young*, *Hartley McGuire*

*   Allow `action_controller.logger` to be disabled by setting it to `nil` or `false` instead of always defaulting to `Rails.logger`.

    *Roberto Miranda*

*   Remove deprecated support to a route to multiple paths.

    *Rafael Mendonça França*

*   Remove deprecated support for using semicolons as a query string separator.

    Before:

    ```ruby
    ActionDispatch::QueryParser.each_pair("foo=bar;baz=quux").to_a
    # => [["foo", "bar"], ["baz", "quux"]]
    ```

    After:

    ```ruby
    ActionDispatch::QueryParser.each_pair("foo=bar;baz=quux").to_a
    # => [["foo", "bar;baz=quux"]]
    ```

    *Rafael Mendonça França*

*   Remove deprecated support to skipping over leading brackets in parameter names in the parameter parser.

    Before:

    ```ruby
    ActionDispatch::ParamBuilder.from_query_string("[foo]=bar") # => { "foo" => "bar" }
    ActionDispatch::ParamBuilder.from_query_string("[foo][bar]=baz") # => { "foo" => { "bar" => "baz" } }
    ```

    After:

    ```ruby
    ActionDispatch::ParamBuilder.from_query_string("[foo]=bar") # => { "[foo]" => "bar" }
    ActionDispatch::ParamBuilder.from_query_string("[foo][bar]=baz") # => { "[foo]" => { "bar" => "baz" } }
    ```

    *Rafael Mendonça França*

*   Deprecate `Rails.application.config.action_dispatch.ignore_leading_brackets`.

    *Rafael Mendonça França*

*   Raise `ActionController::TooManyRequests` error from `ActionController::RateLimiting`

    Requests that exceed the rate limit raise an `ActionController::TooManyRequests` error.
    By default, Action Dispatch rescues the error and responds with a `429 Too Many Requests` status.

    *Sean Doyle*

*   Add .md/.markdown as Markdown extensions and add a default `markdown:` renderer:

    ```ruby
    class Page
      def to_markdown
        body
      end
    end

    class PagesController < ActionController::Base
      def show
        @page = Page.find(params[:id])

        respond_to do |format|
          format.html
          format.md { render markdown: @page }
        end
      end
    end
    ```

    *DHH*

*   Add headers to engine routes inspection command

    *Petrik de Heus*

*   Add "Copy as text" button to error pages

    *Mikkel Malmberg*

*   Add `scope:` option to `rate_limit` method.

    Previously, it was not possible to share a rate limit count between several controllers, since the count was by
    default separate for each controller.

    Now, the `scope:` option solves this problem.

    ```ruby
    class APIController < ActionController::API
      rate_limit to: 2, within: 2.seconds, scope: "api"
    end

    class API::PostsController < APIController
      # ...
    end

    class API::UsersController < APIController
      # ...
    end
    ```

    *ArthurPV*, *Kamil Hanus*

*   Add support for `rack.response_finished` callbacks in ActionDispatch::Executor.

    The executor middleware now supports deferring completion callbacks to later
    in the request lifecycle by utilizing Rack's `rack.response_finished` mechanism,
    when available. This enables applications to define `rack.response_finished` callbacks
    that may rely on state that would be cleaned up by the executor's completion callbacks.

    *Adrianna Chang*, *Hartley McGuire*

*   Produce a log when `rescue_from` is invoked.

    *Steven Webb*, *Jean Boussier*

*   Allow hosts redirects from `hosts` Rails configuration

    ```ruby
    config.action_controller.allowed_redirect_hosts << "example.com"
    ```

    *Kevin Robatel*

*   `rate_limit.action_controller` notification has additional payload

    additional values: count, to, within, by, name, cache_key

    *Jonathan Rochkind*

*   Add JSON support to the built-in health controller.

    The health controller now responds to JSON requests with a structured response
    containing status and timestamp information. This makes it easier for monitoring
    tools and load balancers to consume health check data programmatically.

    ```ruby
    # /up.json
    {
      "status": "up",
      "timestamp": "2025-09-19T12:00:00Z"
    }
    ```

    *Francesco Loreti*, *Juan Vásquez*

*   Allow to open source file with a crash from the browser.

    *Igor Kasyanchuk*

*   Always check query string keys for valid encoding just like values are checked.

    *Casper Smits*

*   Always return empty body for HEAD requests in `PublicExceptions` and
    `DebugExceptions`.

    This is required by `Rack::Lint` (per RFC9110).

    *Hartley McGuire*

*   Add comprehensive support for HTTP Cache-Control request directives according to RFC 9111.

    Provides a `request.cache_control_directives` object that gives access to request cache directives:

    ```ruby
    # Boolean directives
    request.cache_control_directives.only_if_cached?  # => true/false
    request.cache_control_directives.no_cache?        # => true/false
    request.cache_control_directives.no_store?        # => true/false
    request.cache_control_directives.no_transform?    # => true/false

    # Value directives
    request.cache_control_directives.max_age          # => integer or nil
    request.cache_control_directives.max_stale        # => integer or nil (or true for valueless max-stale)
    request.cache_control_directives.min_fresh        # => integer or nil
    request.cache_control_directives.stale_if_error   # => integer or nil

    # Special helpers for max-stale
    request.cache_control_directives.max_stale?         # => true if max-stale present (with or without value)
    request.cache_control_directives.max_stale_unlimited? # => true only for valueless max-stale
    ```

    Example usage:

    ```ruby
    def show
      if request.cache_control_directives.only_if_cached?
        @article = Article.find_cached(params[:id])
        return head(:gateway_timeout) if @article.nil?
      else
        @article = Article.find(params[:id])
      end

      render :show
    end
    ```

    *egg528*

*   Add assert_in_body/assert_not_in_body as the simplest way to check if a piece of text is in the response body.

    *DHH*

*   Include cookie name when calculating maximum allowed size.

    *Hartley McGuire*

*   Implement `must-understand` directive according to RFC 9111.

    The `must-understand` directive indicates that a cache must understand the semantics of the response status code, or discard the response. This directive is enforced to be used only with `no-store` to ensure proper cache behavior.

    ```ruby
    class ArticlesController < ApplicationController
      def show
        @article = Article.find(params[:id])

        if @article.special_format?
          must_understand
          render status: 203 # Non-Authoritative Information
        else
          fresh_when @article
        end
      end
    end
    ```

    *heka1024*

*   The JSON renderer doesn't escape HTML entities or Unicode line separators anymore.

    Using `render json:` will no longer escape `<`, `>`, `&`, `U+2028` and `U+2029` characters that can cause errors
    when the resulting JSON is embedded in JavaScript, or vulnerabilities when the resulting JSON is embedded in HTML.

    Since the renderer is used to return a JSON document as `application/json`, it's typically not necessary to escape
    those characters, and it improves performance.

    Escaping will still occur when the `:callback` option is set, since the JSON is used as JavaScript code in this
    situation (JSONP).

    You can use the `:escape` option or set `config.action_controller.escape_json_responses` to `true` to restore the
    escaping behavior.

    ```ruby
    class PostsController < ApplicationController
      def index
        render json: Post.last(30), escape: true
      end
    end
    ```

    *Étienne Barrié*, *Jean Boussier*

*   Load lazy route sets before inserting test routes

    Without loading lazy route sets early, we miss `after_routes_loaded` callbacks, or risk
    invoking them with the test routes instead of the real ones if another load is triggered by an engine.

    *Gannon McGibbon*

*   Raise `AbstractController::DoubleRenderError` if `head` is called after rendering.

    After this change, invoking `head` will lead to an error if response body is already set:

    ```ruby
    class PostController < ApplicationController
      def index
        render locals: {}
        head :ok
      end
    end
    ```

    *Iaroslav Kurbatov*

*   The Cookie Serializer can now serialize an Active Support SafeBuffer when using message pack.

    Such code would previously produce an error if an application was using messagepack as its cookie serializer.

    ```ruby
    class PostController < ApplicationController
      def index
        flash.notice = t(:hello_html) # This would try to serialize a SafeBuffer, which was not possible.
      end
    end
    ```

    *Edouard Chin*

*   Fix `Rails.application.reload_routes!` from clearing almost all routes.

    When calling `Rails.application.reload_routes!` inside a middleware of
    a Rake task, it was possible under certain conditions that all routes would be cleared.
    If ran inside a middleware, this would result in getting a 404 on most page you visit.
    This issue was only happening in development.

    *Edouard Chin*

*   Add resource name to the `ArgumentError` that's raised when invalid `:only` or `:except` options are given to `#resource` or `#resources`

    This makes it easier to locate the source of the problem, especially for routes drawn by gems.

    Before:
    ```
    :only and :except must include only [:index, :create, :new, :show, :update, :destroy, :edit], but also included [:foo, :bar]
    ```

    After:
    ```
    Route `resources :products` - :only and :except must include only [:index, :create, :new, :show, :update, :destroy, :edit], but also included [:foo, :bar]
    ```

    *Jeremy Green*

*   A route pointing to a non-existing controller now returns a 500 instead of a 404.

    A controller not existing isn't a routing error that should result
    in a 404, but a programming error that should result in a 500 and
    be reported.

    Until recently, this was hard to untangle because of the support
    for dynamic `:controller` segment in routes, but since this is
    deprecated and will be removed in Rails 8.1, we can now easily
    not consider missing controllers as routing errors.

    *Jean Boussier*

*   Add `check_collisions` option to `ActionDispatch::Session::CacheStore`.

    Newly generated session ids use 128 bits of randomness, which is more than
    enough to ensure collisions can't happen, but if you need to harden sessions
    even more, you can enable this option to check in the session store that the id
    is indeed free you can enable that option. This however incurs an extra write
    on session creation.

    *Shia*

*   In ExceptionWrapper, match backtrace lines with built templates more often,
    allowing improved highlighting of errors within do-end blocks in templates.
    Fix for Ruby 3.4 to match new method labels in backtrace.

    *Martin Emde*

*   Allow setting content type with a symbol of the Mime type.

    ```ruby
    # Before
    response.content_type = "text/html"

    # After
    response.content_type = :html
    ```

    *Petrik de Heus*

## Active Job

*   Add structured events for Active Job:
    - `active_job.enqueued`
    - `active_job.bulk_enqueued`
    - `active_job.started`
    - `active_job.completed`
    - `active_job.retry_scheduled`
    - `active_job.retry_stopped`
    - `active_job.discarded`
    - `active_job.interrupt`
    - `active_job.resume`
    - `active_job.step_skipped`
    - `active_job.step_started`
    - `active_job.step`

    *Adrianna Chang*

*   Deprecate built-in `sidekiq` adapter.

    If you're using this adapter, upgrade to `sidekiq` 7.3.3 or later to use the `sidekiq` gem's adapter.

    *fatkodima*

*   Remove deprecated internal `SuckerPunch` adapter in favor of the adapter included with the `sucker_punch` gem.

    *Rafael Mendonça França*

*   Remove support to set `ActiveJob::Base.enqueue_after_transaction_commit` to `:never`, `:always` and `:default`.

    *Rafael Mendonça França*

*   Remove deprecated `Rails.application.config.active_job.enqueue_after_transaction_commit`.

    *Rafael Mendonça França*

*   `ActiveJob::Serializers::ObjectSerializers#klass` method is now public.

    Custom Active Job serializers must have a public `#klass` method too.
    The returned class will be index allowing for faster serialization.

    *Jean Boussier*

*   Allow jobs to the interrupted and resumed with Continuations

    A job can use Continuations by including the `ActiveJob::Continuable`
    concern. Continuations split jobs into steps. When the queuing system
    is shutting down jobs can be interrupted and their progress saved.

    ```ruby
    class ProcessImportJob
      include ActiveJob::Continuable

      def perform(import_id)
        @import = Import.find(import_id)

        # block format
        step :initialize do
          @import.initialize
        end

        # step with cursor, the cursor is saved when the job is interrupted
        step :process do |step|
          @import.records.find_each(start: step.cursor) do |record|
            record.process
            step.advance! from: record.id
          end
        end

        # method format
        step :finalize

        private
          def finalize
            @import.finalize
          end
      end
    end
    ```

    *Donal McBreen*

*   Defer invocation of ActiveJob enqueue callbacks until after commit when
    `enqueue_after_transaction_commit` is enabled.

    *Will Roever*

*   Add `report:` option to `ActiveJob::Base#retry_on` and `#discard_on`

    When the `report:` option is passed, errors will be reported to the error reporter
    before being retried / discarded.

    *Andrew Novoselac*

*   Accept a block for `ActiveJob::ConfiguredJob#perform_later`.

    This was inconsistent with a regular `ActiveJob::Base#perform_later`.

    *fatkodima*

*   Raise a more specific error during deserialization when a previously serialized job class is now unknown.

    `ActiveJob::UnknownJobClassError` will be raised instead of a more generic
    `NameError` to make it easily possible for adapters to tell if the `NameError`
    was raised during job execution or deserialization.

    *Earlopain*

## Action Mailer

*   Add structured events for Action Mailer:
    - `action_mailer.delivered`
    - `action_mailer.processed`

    *Gannon McGibbon*

*   Add `deliver_all_later` to enqueue multiple emails at once.

    ```ruby
    user_emails = User.all.map { |user| Notifier.welcome(user) }
    ActionMailer.deliver_all_later(user_emails)

    # use a custom queue
    ActionMailer.deliver_all_later(user_emails, queue: :my_queue)
    ```

    This can greatly reduce the number of round-trips to the queue datastore.
    For queue adapters that do not implement the `enqueue_all` method, we
    fall back to enqueuing email jobs indvidually.

    *fatkodima*

## Action Cable

*   Allow passing composite channels to `ActionCable::Channel#stream_for` – e.g. `stream_for [ group, group.owner ]`

    *hey-leon*

*   Allow setting nil as subscription connection identifier for Redis.

    *Nguyen Nguyen*

## Active Storage

*   Add structured events for Active Storage:
    - `active_storage.service_upload`
    - `active_storage.service_download`
    - `active_storage.service_streaming_download`
    - `active_storage.preview`
    - `active_storage.service_delete`
    - `active_storage.service_delete_prefixed`
    - `active_storage.service_exist`
    - `active_storage.service_url`
    - `active_storage.service_mirror`

    *Gannon McGibbon*

*   Allow analyzers and variant transformer to be fully configurable

    ```ruby
    # ActiveStorage.analyzers can be set to an empty array:
    config.active_storage.analyzers = []
    # => ActiveStorage.analyzers = []

    # or use custom analyzer:
    config.active_storage.analyzers = [ CustomAnalyzer ]
    # => ActiveStorage.analyzers = [ CustomAnalyzer ]
    ```

    If no configuration is provided, it will use the default analyzers.

    You can also disable variant processor to remove warnings on startup about missing gems.

    ```ruby
    config.active_storage.variant_processor = :disabled
    ```

    *zzak*, *Alexandre Ruban*

*   Remove deprecated `:azure` storage service.

    *Rafael Mendonça França*

*   Remove unnecessary calls to the GCP metadata server.

    Calling Google::Auth.get_application_default triggers an explicit call to
    the metadata server - given it was being called for significant number of
    file operations, it can lead to considerable tail latencies and even metadata
    server overloads. Instead, it's preferable (and significantly more efficient)
    that applications use:

    ```ruby
    Google::Apis::RequestOptions.default.authorization = Google::Auth.get_application_default(...)
    ```

    In the cases applications do not set that, the GCP libraries automatically determine credentials.

    This also enables using credentials other than those of the associated GCP
    service account like when using impersonation.

    *Alex Coomans*

*   Direct upload progress accounts for server processing time.

    *Jeremy Daer*

*   Delegate `ActiveStorage::Filename#to_str` to `#to_s`

    Supports checking String equality:

    ```ruby
    filename = ActiveStorage::Filename.new("file.txt")
    filename == "file.txt" # => true
    filename in "file.txt" # => true
    "file.txt" == filename # => true
    ```

    *Sean Doyle*

*   A Blob will no longer autosave associated Attachment.

    This fixes an issue where a record with an attachment would have
    its dirty attributes reset, preventing your `after commit` callbacks
    on that record to behave as expected.

    Note that this change doesn't require any changes on your application
    and is supposed to be internal. Active Storage Attachment will continue
    to be autosaved (through a different relation).

    *Edouard-chin*

## Action Mailbox

*   Add `reply_to_address` extension method on `Mail::Message`.

    *Mr0grog*

## Action Text

*   De-couple `@rails/actiontext/attachment_upload.js` from `Trix.Attachment`

    Implement `@rails/actiontext/index.js` with a `direct-upload:progress` event
    listeners and `Promise` resolution.

    *Sean Doyle*

*   Capture block content for form helper methods

    ```erb
    <%= rich_textarea_tag :content, nil do %>
      <h1>hello world</h1>
    <% end %>
    <!-- <input type="hidden" name="content" id="trix_input_1" value="&lt;h1&gt;hello world&lt;/h1&gt;"/><trix-editor … -->

    <%= rich_textarea :message, :content, input: "trix_input_1" do %>
      <h1>hello world</h1>
    <% end %>
    <!-- <input type="hidden" name="message[content]" id="trix_input_1" value="&lt;h1&gt;hello world&lt;/h1&gt;"/><trix-editor … -->

    <%= form_with model: Message.new do |form| %>
      <%= form.rich_textarea :content do %>
        <h1>hello world</h1>
      <% end %>
    <% end %>
    <!-- <form action="/messages" accept-charset="UTF-8" method="post"><input type="hidden" name="message[content]" id="message_content_trix_input_message" value="&lt;h1&gt;hello world&lt;/h1&gt;"/><trix-editor … -->
    ```

    *Sean Doyle*

*   Generalize `:rich_text_area` Capybara selector

    Prepare for more Action Text-capable WYSIWYG editors by making
    `:rich_text_area` rely on the presence of `[role="textbox"]` and
    `[contenteditable]` HTML attributes rather than a `<trix-editor>` element.

    *Sean Doyle*

*   Forward `fill_in_rich_text_area` options to Capybara

    ```ruby
    fill_in_rich_textarea "Rich text editor", id: "trix_editor_1", with: "Hello world!"
    ```

    *Sean Doyle*

*   Attachment upload progress accounts for server processing time.

    *Jeremy Daer*

*   The Trix dependency is now satisfied by a gem, `action_text-trix`, rather than vendored
    files. This allows applications to bump Trix versions independently of Rails
    releases. Effectively this also upgrades Trix to `>= 2.1.15`.

    *Mike Dalessio*

*   Change `ActionText::RichText#embeds` assignment from `before_save` to `before_validation`

    *Sean Doyle*

## Railties

*   Suggest `bin/rails action_text:install` from Action Dispatch error page

    *Sean Doyle*

*   Remove deprecated `STATS_DIRECTORIES`.

    *Rafael Mendonça França*

*   Remove deprecated `bin/rake stats` command.

    *Rafael Mendonça França*

*   Remove deprecated `rails/console/methods.rb` file.

    *Rafael Mendonça França*

*   Don't generate system tests by default.

    Rails scaffold generator will no longer generate system tests by default. To enable this pass `--system-tests=true` or generate them with `bin/rails generate system_test name_of_test`.

    *Eileen M. Uchitelle*

*   Optionally skip bundler-audit.

    Skips adding the `bin/bundler-audit` & `config/bundler-audit.yml` if the gem is not installed when `bin/rails app:update` runs.

    Passes an option to `--skip-bundler-audit` when new apps are generated & adds that same option to the `--minimal` generator flag.

    *Jill Klang*

*   Show engine routes in `/rails/info/routes` as well.

    *Petrik de Heus*

*   Exclude `asset_path` configuration from Kamal `deploy.yml` for API applications.

    API applications don't serve assets, so the `asset_path` configuration in `deploy.yml`
    is not needed and can cause 404 errors on in-flight requests. The asset_path is now
    only included for regular Rails applications that serve assets.

    *Saiqul Haq*

*   Reverted the incorrect default `config.public_file_server.headers` config.

    If you created a new application using Rails `8.1.0.beta1`, make sure to regenerate
    `config/environments/production.rb`, or to manually edit the `config.public_file_server.headers`
    configuration to just be:

    ```ruby
    # Cache assets for far-future expiry since they are all digest stamped.
    config.public_file_server.headers = { "cache-control" => "public, max-age=#{1.year.to_i}" }
    ```

    *Jean Boussier*

*   Add command `rails credentials:fetch PATH` to get the value of a credential from the credentials file.

    ```bash
    $ bin/rails credentials:fetch kamal_registry.password
    ```

    *Matthew Nguyen*, *Jean Boussier*

*   Generate static BCrypt password digests in fixtures instead of dynamic ERB expressions.

    Previously, fixtures with password digest attributes used `<%= BCrypt::Password.create("secret") %>`,
    which regenerated the hash on each test run. Now generates a static hash with a comment
    showing how to recreate it.

    *Nate Smith*, *Cassia Scheffer*

*   Broaden the `.gitignore` entry when adding a credentials key to ignore all key files.

    *Greg Molnar*

*   Remove unnecessary `ruby-version` input from `ruby/setup-ruby`

    *TangRufus*

*   Add --reset option to bin/setup which will call db:reset as part of the setup.

    *DHH*

*   Add RuboCop cache restoration to RuboCop job in GitHub Actions workflow templates.

    *Lovro Bikić*

*   Skip generating mailer-related files in authentication generator if the application does
    not use ActionMailer

    *Rami Massoud*

*   Introduce `bin/ci` for running your tests, style checks, and security audits locally or in the cloud.

    The specific steps are defined by a new DSL in `config/ci.rb`.

    ```ruby
    ActiveSupport::ContinuousIntegration.run do
      step "Setup", "bin/setup --skip-server"
      step "Style: Ruby", "bin/rubocop"
      step "Security: Gem audit", "bin/bundler-audit"
      step "Tests: Rails", "bin/rails test test:system"
    end
    ```

    Optionally use [gh-signoff](https://github.com/basecamp/gh-signoff) to
    set a green PR status - ready for merge.

    *Jeremy Daer*, *DHH*

*   Generate session controller tests when running the authentication generator.

    *Jerome Dalbert*

*   Add bin/bundler-audit and config/bundler-audit.yml for discovering and managing known security problems with app gems.

    *DHH*

*   Rails no longer generates a `bin/bundle` binstub when creating new applications.

    The `bin/bundle` binstub used to help activate the right version of bundler.
    This is no longer necessary as this mechanism is now part of Rubygem itself.

    *Edouard Chin*

*   Add a `SessionTestHelper` module with `sign_in_as(user)` and `sign_out` test helpers when
    running `rails g authentication`. Simplifies authentication in integration tests.

    *Bijan Rahnema*

*   Rate limit password resets in authentication generator

    This helps mitigate abuse from attackers spamming the password reset form.

    *Chris Oliver*

*   Update `rails new --minimal` option

    Extend the `--minimal` flag to exclude recently added features:
    `skip_brakeman`, `skip_ci`, `skip_docker`, `skip_kamal`, `skip_rubocop`, `skip_solid` and `skip_thruster`.

    *eelcoj*

*   Add `application-name` metadata to application layout

    The following metatag will be added to `app/views/layouts/application.html.erb`

    ```html
    <meta name="application-name" content="Name of Rails Application">
    ```

    *Steve Polito*

*   Use `secret_key_base` from ENV or credentials when present locally.

    When ENV["SECRET_KEY_BASE"] or
    `Rails.application.credentials.secret_key_base` is set for test or
    development, it is used for the `Rails.config.secret_key_base`,
    instead of generating a `tmp/local_secret.txt` file.

    *Petrik de Heus*

*   Introduce `RAILS_MASTER_KEY` placeholder in generated ci.yml files

    *Steve Polito*

*   Colorize the Rails console prompt even on non standard environments.

    *Lorenzo Zabot*

*   Don't enable YJIT in development and test environments

    Development and test environments tend to reload code and redefine methods (e.g. mocking),
    hence YJIT isn't generally faster in these environments.

    *Ali Ismayilov*, *Jean Boussier*

*   Only include PermissionsPolicy::Middleware if policy is configured.

    *Petrik de Heus*

## Guides

*   In the Active Job bug report template set the queue adapter to the
    test adapter so that `assert_enqueued_with` can pass.

    *Andrew White*

*   Ensure all bug report templates set `config.secret_key_base` to avoid
    generation of `tmp/local_secret.txt` files when running the report template.

    *Andrew White*

## 8.0.3
- Tag: `v8.0.3`
- Published: 2025-09-22
- URL: https://github.com/rails/rails/releases/tag/v8.0.3

## Active Support

*   `ActiveSupport::FileUpdateChecker` does not depend on `Time.now` to prevent unnecessary reloads with time travel test helpers

    *Jan Grodowski*

*   Fix `ActiveSupport::BroadcastLogger` from executing a block argument for each logger (tagged, info, etc.).

    *Jared Armstrong*

*   Make `ActiveSupport::Logger` `#freeze`-friendly.

    *Joshua Young*

*   Fix `ActiveSupport::HashWithIndifferentAccess#transform_keys!` removing defaults.

    *Hartley McGuire*

*   Fix `ActiveSupport::HashWithIndifferentAccess#tranform_keys!` to handle collisions.

    If the transformation would result in a key equal to another not yet transformed one,
    it would result in keys being lost.

    Before:

    ```ruby
    >> {a: 1, b: 2}.with_indifferent_access.transform_keys!(&:succ)
    => {"c" => 1}
    ```

    After:

    ```ruby
    >> {a: 1, b: 2}.with_indifferent_access.transform_keys!(&:succ)
    => {"c" => 1, "d" => 2}
    ```

    *Jason T Johnson*, *Jean Boussier*

*   Fix `ActiveSupport::Cache::MemCacheStore#read_multi` to handle network errors.

    This method specifically wasn't handling network errors like other codepaths.

    *Alessandro Dal Grande*

*   Fix configuring `RedisCacheStore` with `raw: true`.

    *fatkodima*

*   Fix `Enumerable#sole` for infinite collections.

    *fatkodima*


## Active Model

*   Fix `has_secure_password` to perform confirmation validation of the password even when blank.

    The validation was incorrectly skipped when the password only contained whitespace characters.

    *Fabio Sangiovanni*


## Active Record

*   Fix query cache for pinned connections in multi threaded transactional tests

    When a pinned connection is used across separate threads, they now use a separate cache store
    for each thread.

    This improve accuracy of system tests, and any test using multiple threads.

    *Heinrich Lee Yu*, *Jean Boussier*

*   Don't add `id_value` attribute alias when attribute/column with that name already exists.

    *Rob Lewis*

*   Fix false positive change detection involving STI and polymorphic has one relationships.

    Polymorphic `has_one` relationships would always be considered changed when defined in a STI child
    class, causing nedless extra autosaves.

    *David Fritsch*

*   Skip calling `PG::Connection#cancel` in `cancel_any_running_query`
    when using libpq >= 18 with pg < 1.6.0, due to incompatibility.
    Rollback still runs, but may take longer.

    *Yasuo Honda*, *Lars Kanis*

*   Fix stale association detection for polymorphic `belongs_to`.

    *Florent Beaurain*, *Thomas Crambert*

*   Fix removal of PostgreSQL version comments in `structure.sql` for latest PostgreSQL versions which include `\restrict`

    *Brendan Weibrecht*

*   Allow setting `schema_format` in database configuration.

    ```
    primary:
      schema_format: ruby
    ```

    Useful in multi-database setups to have different formats per-database.

    *T S Vallender*

*   Use ntuples to populate row_count instead of count for Postgres

    *Jonathan Calvert*

*   Fix `#merge` with `#or` or `#and` and a mixture of attributes and SQL strings resulting in an incorrect query.

    ```ruby
    base = Comment.joins(:post).where(user_id: 1).where("recent = 1")
    puts base.merge(base.where(draft: true).or(Post.where(archived: true))).to_sql
    ```

    Before:

    ```SQL
    SELECT "comments".* FROM "comments"
    INNER JOIN "posts" ON "posts"."id" = "comments"."post_id"
    WHERE (recent = 1)
    AND (
      "comments"."user_id" = 1
      AND (recent = 1)
      AND "comments"."draft" = 1
      OR "posts"."archived" = 1
    )
    ```

    After:

    ```SQL
    SELECT "comments".* FROM "comments"
    INNER JOIN "posts" ON "posts"."id" = "comments"."post_id"
    WHERE "comments"."user_id" = 1
    AND (recent = 1)
    AND (
      "comments"."user_id" = 1
      AND (recent = 1)
      AND "comments"."draft" = 1
      OR "posts"."archived" = 1
    )
    ```

    *Joshua Young*

*   Fix inline `has_and_belongs_to_many` fixtures for tables with composite primary keys.

    *fatkodima*

*   Fix migration log message for down operations.

    *Bernardo Barreto*

*   Prepend `extra_flags` in postgres' `structure_load`

    When specifying `structure_load_flags` with a postgres adapter, the flags
    were appended to the default flags, instead of prepended.
    This caused issues with flags not being taken into account by postgres.

    *Alice Loeser*

*   Fix `annotate` comments to propagate to `update_all`/`delete_all`.

    *fatkodima*

*   Fix checking whether an unpersisted record is `include?`d in a strictly
    loaded `has_and_belongs_to_many` association.

    *Hartley McGuire*

*   `create_or_find_by` will now correctly rollback a transaction.

    When using `create_or_find_by`, raising a ActiveRecord::Rollback error
    in a `after_save` callback had no effect, the transaction was committed
    and a record created.

    *Edouard Chin*

*   Gracefully handle `Timeout.timeout` firing during connection configuration.

    Use of `Timeout.timeout` could result in improperly initialized database connection.

    This could lead to a partially configured connection being used, resulting in various exceptions,
    the most common being with the PostgreSQLAdapter raising `undefined method 'key?' for nil`
    or `TypeError: wrong argument type nil (expected PG::TypeMap)`.

    *Jean Boussier*

*   Fix stale state for composite foreign keys in belongs_to associations.

    *Varun Sharma*


## Action View

*   Fix label with `for` option not getting prefixed by form `namespace` value

    *Abeid Ahmed*, *Hartley McGuire*

*   Fix `javascript_include_tag` `type` option to accept either strings and symbols.

    ```ruby
    javascript_include_tag "application", type: :module
    javascript_include_tag "application", type: "module"
    ```

    Previously, only the string value was recognized.

    *Jean Boussier*

*   Fix `excerpt` helper with non-whitespace separator.

    *Jonathan Hefner*


## Action Pack

*   URL helpers for engines mounted at the application root handle `SCRIPT_NAME` correctly.

    Fixed an issue where `SCRIPT_NAME` is not applied to paths generated for routes in an engine
    mounted at "/".

    *Mike Dalessio*

*   Fix `Rails.application.reload_routes!` from clearing almost all routes.

    When calling `Rails.application.reload_routes!` inside a middleware of
    a Rake task, it was possible under certain conditions that all routes would be cleared.
    If ran inside a middleware, this would result in getting a 404 on most page you visit.
    This issue was only happening in development.

    *Edouard Chin*

*   Address `rack 3.2` deprecations warnings.

    ```
    warning: Status code :unprocessable_entity is deprecated and will be removed in a future version of Rack.
    Please use :unprocessable_content instead.
    ```

    Rails API will transparently convert one into the other for the foreseeable future.

    *Earlopain*, *Jean Boussier*

*   Support hash-source in Content Security Policy.

    *madogiwa*

*   Always return empty body for HEAD requests in `PublicExceptions` and
    `DebugExceptions`.

    This is required by `Rack::Lint` (per RFC9110).

    *Hartley McGuire*


## Active Job

*   Include the actual Active Job locale when serializing rather than I18n locale.

    *Adrien S*

*   Fix `retry_job` instrumentation when using `:test` adapter for Active Job.

    *fatkodima*


## Action Mailer

*   No changes.


## Action Cable

*   Fixed compatibility with `redis` gem `5.4.1`

    *Jean Boussier*

*   Fixed a possible race condition in `stream_from`.

    *OuYangJinTing*


## Active Storage

*   Address deprecation of `Aws::S3::Object#upload_stream` in `ActiveStorage::Service::S3Service`.

    *Joshua Young*

*   Fix `config.active_storage.touch_attachment_records` to work with eager loading.

    *fatkodima*


## Action Mailbox

*   No changes.


## Action Text

*   Add rollup-plugin-terser as a dev dependency.

    *Édouard Chin*


## Railties

*   Fix `polymorphic_url` and `polymorphic_path` not working when routes are not loaded.

    *Édouard Chin*

*   Fix Rails console to not override user defined IRB_NAME.

    Only change the prompt name if it hasn't been customized in `.irbrc`.

    *Jarrett Lusso*


## Guides

*   No changes.

## 8.0.2.1
- Tag: `v8.0.2.1`
- Published: 2025-08-13
- URL: https://github.com/rails/rails/releases/tag/v8.0.2.1

## Active Support

*   No changes.


## Active Model

*   No changes.


## Active Record

*   Call inspect on ids in RecordNotFound error

    [CVE-2025-55193]

    *Gannon McGibbon*, *John Hawthorn*

## Action View

*   No changes.


## Action Pack

*   No changes.


## Active Job

*   No changes.


## Action Mailer

*   No changes.


## Action Cable

*   No changes.


## Active Storage

    Remove dangerous transformations

    [CVE-2025-24293]

    *Zack Deveau*

## Action Mailbox

*   No changes.


## Action Text

*   No changes.


## Railties

*   No changes.


## Guides

*   No changes.
